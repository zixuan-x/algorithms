# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = [0]
        self.search(root, result)
        return result[0] - 1  # 数edge，不是数node
    
        
    def search(self, root, result) -> int:
        '''
        Return max length of univalue paths starting at root
        '''
        if not root:
            return 0
        
        left = self.search(root.left, result)
        right = self.search(root.right, result)
        
        if root.left and root.left.val != root.val:
            left = 0
        if root.right and root.right.val != root.val:
            right = 0
        
        result[0] = max(result[0], left + right + 1)
        
        return max(left, right) + 1       
        
        
        