# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[1]
    
    def dfs(self, root):
        '''return height and node'''
        if not root:
            return 0, root
        
        h1, node1 = self.dfs(root.left)
        h2, node2 = self.dfs(root.right)
        
        if h1 > h2:
            return h1 + 1, node1
        elif h1 < h2:
            return h2 + 1, node2
        else:
            return h1 + 1, root