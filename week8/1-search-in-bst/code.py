# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None or root.val == val:
            return root
        
        # Если искомое значение меньше текущего, идём только влево
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # Иначе искомое значение больше текущего идём только вправо
        return self.searchBST(root.right, val)
        
