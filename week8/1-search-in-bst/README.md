# 700. Search in a Binary Search Tree

## 1. Problem
We have a Binary Search Tree (BST) and a target number `val`. We need to find the node with `val` and return it (along with its subtree). If the value is not in the tree, return `None`.

## 2. Approach

### How It Works
In a BST, smaller numbers are always on the left, and bigger numbers are always on the right. Because of this, we do not need to check every node:
1. If the current node is `None` or equals `val`, return it.
2. If `val` is smaller than the current node, search only the left side.
3. If `val` is bigger than the current node, search only the right side.

### Tracing Examples
Tree: `[4, 2, 7, 1, 3]`

* **Example 1 (`val = 2`):**
  * Start at `4`: `2 < 4`, so go left to `2`.
  * At `2`: `2 == 2` (match found). Return node `2` (`[2, 1, 3]`).
* **Example 2 (`val = 5`):**
  * Start at `4`: `5 > 4`, so go right to `7`.
  * At `7`: `5 < 7`, so go left to `None`.
  * At `None`: return `None` (`[]`).

### Challenges
* At first, I thought about checking every node one by one, which ignores the BST structure and wastes time.
* While coding, I checked `root.val == val` before `root is None`. This caused an error when hitting empty leaves. Putting `root is None` first fixed it.

## 3. Time & Space Complexity
* **Time Complexity: `O(h)`** (`h` is the height of the tree). At each step, we go down one level and skip half the remaining tree. This is `O(log n)` for a balanced tree and `O(n)` in the worst case (a straight-line tree).
* **Space Complexity: `O(h)`** because each recursive call uses memory on the call stack (`O(log n)` average, `O(n)` worst case).

## 4. Reflection / Improvement
* **Can it be more efficient?** Yes, we can use less memory.
* **What to change?** Replace recursion with a `while` loop that moves a pointer down the tree (`current = current.left` or `current.right`).
* **New complexity:** Time stays `O(h)`, and Space improves to `O(1)`.
