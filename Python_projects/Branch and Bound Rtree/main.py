import time
import tqdm
from rtree import Rtree
from utils import branch_and_bound_skyline, load_data, sequential_search, save_skyline, divide_and_conquer 

if __name__ == '__main__':
    # Load data
    data = load_data("city1.txt")
    print("Seqeuntial skyline computation")
    start = time.time()
    sequential_skyline = sequential_search(data)
    sequential_time = time.time() - start
    print("Sequential skyline computation took %.4f seconds" % sequential_time)
    save_skyline(sequential_skyline, sequential_time, "res/skyline_seq.txt")

    # R-tree skyline computation
    print("Constructing R-tree")
    rtree = Rtree()
    for point in tqdm.tqdm(data):
        rtree.insert(rtree.root, point)

    start = time.time()
    rtree_skyline = branch_and_bound_skyline(rtree.root)
    rtree_time = time.time() - start
    print("R-tree branch and bound skyline computation took ", rtree_time, "seconds")
    save_skyline(rtree_skyline, rtree_time, "res/skyline_bbs.txt")

    # Divide and Conquer
    divide_conquer_skyline, divide_conquer_time = divide_and_conquer(data)
    print("Divide and Conquer skyline computation took ", divide_conquer_time, "seconds")
    save_skyline(divide_conquer_skyline, divide_conquer_time, "res/skyline_dc.txt")




    