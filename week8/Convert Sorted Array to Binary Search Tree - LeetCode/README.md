# 108. Convert Sorted Array to Binary Search Tree

## 1. Problem
Given a sorted array `nums` in ascending order, turn it into a height-balanced Binary Search Tree (a tree where the left and right sides of every node differ in height by at most 1).

## 2. Approach

### How It Works
Because the array is already sorted, picking the middle element as the root puts half the numbers on the left and half on the right. This keeps the tree balanced:
1. Track the current subarray using `left` and `right` indices.
2. If `left > right`, there are no numbers left, so return `None`.
3. Find the middle index `mid = (left + right) // 2` and create a node with `nums[mid]`.
4. Recursively build the left child from `left` to `mid - 1` and the right child from `mid + 1` to `right`.

### Tracing Examples
Array: `nums = [-10, -3, 0, 5, 9]` (indices `0` to `4`)

* **`build(0, 4)`:** `mid = 2` -> Root is `0`.
* **Left — `build(0, 1)`:** `mid = 0` -> Node is `-10`.
  * Left `build(0, -1)` -> `None`.
  * Right `build(1, 1)` -> `mid = 1` -> Leaf node is `-3`.
* **Right — `build(3, 4)`:** `mid = 3` -> Node is `5`.
  * Left `build(3, 2)` -> `None`.
  * Right `build(4, 4)` -> `mid = 4` -> Leaf node is `9`.
* **Result:** Balanced BST `[0, -10, 5, null, -3, null, 9]`.

### Challenges
* At first, I used list slicing (`nums[:mid]`), which copied parts of the array on every call and slowed the code down to `O(n log n)`. Passing `left` and `right` indices avoided copying and fixed this.
* I initially wrote `if left >= right: return None`, which skipped single elements and missed all leaf nodes. Changing it to `left > right` solved the problem.

## 3. Time & Space Complexity
* **Time Complexity: `O(n)`** (`n` is the length of `nums`). Every element becomes the middle index once, and creating each node takes `O(1)` time.
* **Space Complexity: `O(log n)`** extra space for the recursion stack (since the tree is balanced, its height is `log n`), plus `O(n)` to store the output tree itself.

## 4. Reflection / Improvement
* **Can it be more efficient?** `O(n)` time and `O(log n)` extra space is already optimal because every number must be visited once.
* **What to change?** For very large arrays, we could replace recursion with a `while` loop and our own stack/queue to avoid hitting Python's recursion limit.
* **New complexity:** Time stays `O(n)`, and extra Space stays `O(log n)` (with a stack) or `O(n)` (with a queue).
