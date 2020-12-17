# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res)
        return max(res)
    
    def dfs(self, root, res):
        if not root:
            return 0, 0
        
        inc, dec = 1, 1
        l_inc, l_dec = self.dfs(root.left, res)
        r_inc, r_dec = self.dfs(root.right, res)
        if root.left:
            if root.left.val == root.val + 1:
                inc = max(inc, l_inc + 1)
            if root.left.val == root.val - 1:
                dec = max(dec, l_dec + 1)
        if root.right:
            if root.right.val == root.val + 1:
                inc = max(inc, r_inc + 1)
            if root.right.val == root.val - 1:
                dec = max(dec, r_dec + 1)
    
        res[0] = max(res[0], inc + dec - 1)
        return inc, dec
        
        