# 938. Range Sum of BST

## 1. Problem
Given a Binary Search Tree (BST) and two numbers `low` and `high`, return the sum of all node values that are between `low` and `high` (including both `low` and `high`).

## 2. Approach

### How It Works
Instead of visiting every node, we use BST rules to skip branches that cannot have valid numbers:
1. If the node is `None`, return `0`.
2. If `root.val < low`, skip the left branch (all values there are even smaller) and only check the right branch.
3. If `root.val > high`, skip the right branch (all values there are even bigger) and only check the left branch.
4. If `root.val` is inside `[low, high]`, add `root.val` to the sum and check both left and right branches.

### Tracing Examples
Tree: `[10, 5, 15, 3, 7, null, 18]`, `low = 7`, `high = 15`

* **Node `10`:** Inside `[7, 15]`. Keep `10`, check left and right.
* **Node `5` (left):** `5 < 7`, so skip `3` and go right to `7`.
* **Node `7`:** Inside `[7, 15]`. Keep `7`. Children are `None` (`0`).
* **Node `15` (right):** Inside `[7, 15]`. Keep `15`, go right to `18`.
* **Node `18`:** `18 > 15`, so skip right and go left (`None` -> `0`).
* **Final Sum:** `10 + 7 + 15 = 32`.

### Challenges
* First, I wrote a basic search that visited every node without skipping anything. Adding the `< low` and `> high` checks made it skip useless branches.
* At first, I wrote `<= low` instead of `< low`, which accidentally skipped `7` because `7 == low`. Changing it to strict `<` and `>` fixed the bug.

## 3. Time & Space Complexity
* **Time Complexity: `O(n)`** (`n` is the number of nodes). Even though we skip branches, in the worst case all nodes fall inside `[low, high]`, so we still have to visit every node once.
* **Space Complexity: `O(h)`** (`h` is the tree height) because of the recursion call stack (`O(log n)` for a balanced tree, `O(n)` for a skewed tree).

## 4. Reflection / Improvement
* **Can it be more efficient?** Worst-case time (`O(n)`) cannot be improved, but we can save memory.
* **What to change?** Use **Morris Traversal** (an iterative method without recursion or a stack) to walk through the tree.
* **New complexity:** Time stays `O(n)`, and Space improves to `O(1)`.
