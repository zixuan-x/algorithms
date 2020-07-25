# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, p, q):
        if not p or not q:
            return p == q
        
        return p.val == q.val and self.compare(p.left, q.right) and self.compare(p.right, q.left)
        