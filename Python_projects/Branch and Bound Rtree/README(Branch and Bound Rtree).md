# 🌇 Skyline Query Project — Exploring Smarter Data Filtering

Have you ever wanted to find the *best* options from a sea of choices — like the cheapest AND closest hotel, or a job with the highest salary AND shortest commute? That’s where **skyline queries** come in.

This project explores how we can efficiently find such optimal choices from a dataset using three different algorithms. We compare their performance and logic to better understand how to work with multi-dimensional decision-making.

---

## 💡 What is a Skyline Query?

A **skyline query** returns all data points that are **not dominated** by any other point. In simple terms, these are the points that are *the best in at least one aspect, and not worse in others*.

For example, if you're picking a restaurant based on **price** and **distance**, a skyline point is one where **no other place is both cheaper and closer**.

---

## 🛠 What This Project Does

We load a 2D dataset (like points on a map) and find the skyline using three different approaches:

| Method                  | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| ✅ **Sequential Scan**   | A basic, brute-force method that checks each point against all others.     |
| 🌲 **R-Tree + Branch & Bound** | A smarter, spatial indexing method that avoids unnecessary comparisons. |
| 🔀 **Divide & Conquer** | Breaks the problem into smaller parts and merges the results.              |

Each method is timed, and the skyline points are saved for review and comparison.

---

## 📁 Project Structure

```
.
├── main.py              # Main script: runs all 3 skyline methods
├── RTree.py             # Custom-built R-Tree logic
├── utils.py             # Helper functions (e.g. dominance check, merging)
├── city1.txt            # Sample dataset: a list of 2D points with IDs
└── res/
    ├── skyline_seq.txt  # Output from Sequential Search
    ├── skyline_bbs.txt  # Output from R-Tree Branch and Bound
    └── skyline_dc.txt   # Output from Divide and Conquer
```

---

## 📦 How to Run It

1. Make sure Python 3 is installed.
2. Install dependencies:
   ```bash
   pip install numpy rtree tqdm
   ```
3. Run the project:
   ```bash
   python main.py
   ```

Skyline results and timing for each method will be saved in the `res/` folder.

---

## 🧪 Real-World Applications

Skyline queries are useful in:
- **Travel apps**: Finding flights that are fastest and cheapest.
- **E-commerce**: Filtering products that are both highly rated and affordable.
- **Real estate**: Identifying properties that are big and close to transit, but not overpriced.

Instead of manually setting hard filters, skyline queries let users see the “best trade-off” options without needing to decide what matters most upfront.

---

## 🧠 Why Compare Methods?

As datasets grow, performance matters. A brute-force method might be okay for 100 records, but not for 10,000. This project lets us:
- Understand trade-offs between simplicity and performance.
- Learn how spatial data structures like R-Trees help us **think spatially**.
- Practice building and testing algorithms for **multi-criteria filtering**.

---

## 📝 Example Input Format (`city1.txt`)

```
ID  X     Y
1   23.4  45.1
2   30.0  40.5
3   20.1  47.0
...
```

---

## 📬 Feedback & Contributions

This is a learning project — if you spot bugs or want to improve the merging in the divide-and-conquer method, feel free to reach out or fork and play around!

Happy skyline searching ✨
