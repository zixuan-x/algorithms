# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))
        
    def isValid(self, root, left, right):
        if not root:
            return True
        
        return left < root.val < right and self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right)
        