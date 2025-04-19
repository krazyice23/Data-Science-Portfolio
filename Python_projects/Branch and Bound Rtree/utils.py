from rtree import index
import numpy as np
import RTree as RTree
from rtree import Rtree

global points
points = []
count = 0

# def load_data():
with open('city1.txt', 'r') as dataset:
        for data in dataset.readlines():
            data = data.split()
            points.append({ #https://www.w3schools.com/python/ref_list_append.asp
                'id': int(data[0]),
                'x': float(data[1]),
                'y': float(data[2])
                   })
            count =+ 1

def dominates(p1, p2):
    # Check if point p1 dominates point p2.
    # param p1: A tuple representing the first point (x1, y1)
    # param p2: A tuple representing the second point (x2, y2)
    # return True if p1 dominates p2, False otherwise
    return (p1[0] <= p2[0] and p1[1] <= p2[1]) and (p1[0] < p2[0] or p1[1] < p2[1])

def find_skyline():
    global data
    skyline = [] # Initialize the skyline points
    for node in data: # Loop through node in data using a for loop
        dominated = False # Create a variable dominated and set it to False
        for other_node in data: # Loop through other_node in data using a for loop 
            if dominates(node, other_node): # If node dominates other_node
                dominated = True # Set dominated to True
                break # Break
        if not dominated: # If not dominated, add node to skyline
            skyline.append(node) # Add node to skyline list
    return skyline # Return skyline
    
# def sequential_search(data): # Find the skyline points using a sequential scan method
#     # The param, points is a list of tuples where each tuple represents a point in the multi-dimensional space
#     skyline_points = [] # Initiate an empty list of skyline points
#     for p in data: # Create a for loop that loops through point in points
#         dominated = False # Create a variable dominated and set it to False
#         non_dominating_points = [] # Initiate an empty list of non-dominating points
#         for q in skyline_points: # Create a for loop that loops through sky_point in skyline_points
#             if dominates(p, q): # If point dominates sky_point, sky_point is not a skyline point
#                 continue  # If the current point dominates a skyline point, remove the dominated skyline point
#             if dominates(q, p):
#                 dominated = True # Set dominated to True
#                 break # Break out of the for loop when the if condition is met
#             non_dominating_points.append(q) # If neither point dominates the other, keep the skyline point
#         if not dominated: 
#             non_dominating_points.append(p) # If not dominated, keep the point
#         skyline_points = non_dominating_points # assign variable skyline_points to non-dominating_points 
#     return skyline_points # return skyline_points list

def branch_and_bound_skyline(points): # Compute the skyline using the branch-and-bound algorithm with an R-tree
    # Create an R-tree index
    p = index.Property() # https://realpython.com/python-property/#:~:text=Python
    p.dimension = len(points[0]) # Dimensionality
    rtree_idx = index.Index(properties=p) 
    
    # Insert points into the R-tree
    for i, point in enumerate(points):
        rtree_idx.insert(i, point + point)  # R-tree expects (id, bounding box)
    
    # Initialize the skyline list
    skyline = []

    # Traverse the R-tree using a branch-and-bound approach
    for i in rtree_idx.intersection(rtree_idx.bounds, objects=True):
        p1 = points[i.id]
        dominated = False # Set dominated intially to False
        to_remove = [] # Create a list to store all data points that have been removed
        
        for s in skyline: # Loop the data points p1 through skyline list
            if dominates(p1, s): # If p1 dominates p2 
                dominated = True # Set dominated to True
                break # Break out of the for loop when the if condition is met 
            if dominates(s, p1): # If p2 dominates p1
                to_remove.append(s) # Add p1 to to_remove list
        
        if not dominated: # If not dominated
            skyline.append(p1) # Add p2 to skyline
            for s in to_remove: # Loop the data points p1 through to_remove list
                skyline.remove(s) # Remove p1 from skyline
    return skyline # Return skyline list

# with open('city1.txt', 'r') as file_1:
#         read = file_1.read()

# data = read

def divide_dataset(data):
    global count
    # data = load_data()
    # median = np.median(data[0])
    # subspace1 = data[data[0] <= median]
    # subspace2 = data[data[0] > median]
    # return subspace1, subspace2
    subspace1 = []
    subspace2 = []
    median = (data[count-1]['x'] + data[0]['x'])/2
    for point in data:
        if point['x'] < median:
            subspace1.append(point)
        else:
            subspace2.append(point)
    return subspace1, subspace2

def divide_and_conquer(data):
    rtree = Rtree()
    for point in data:
        rtree.insert(rtree.root, (point['x'], point['y'], point['x'], point['y']))
    
    skyline = []
    for idx in rtree.intersection((float('-inf'), float('-inf'), float('inf'), float('inf')), objects=True):
        point = data[idx.object]
        if not any(all(point <= s) for s in skyline):
            skyline.append(point)
    return np.array(skyline), 0  # Assuming 0 is the placeholder for time


def final_skyline(skyline1, skyline2):
    combined_skyline = np.vstack((skyline1, skyline2))
    final_skyline = []
    for point in combined_skyline:
        if not any(all(point <= s) for s in final_skyline):
            final_skyline.append(point)
    return np.array(final_skyline)

# Divide the dataset
subspace1, subspace2 = divide_dataset(points)

# Build R-Trees
rtree1 = RTree
rtree2 = RTree

# Find skylines
skyline1 = divide_and_conquer(subspace1)
skyline2 = divide_and_conquer(subspace2)
   

# Combine skylines to find the final skyline
final_skyline_points = final_skyline(skyline1, skyline2)




                    