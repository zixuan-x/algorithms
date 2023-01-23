# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]
        self.dfs(root, 0, root.val, res)
        return res[0]
    
    def dfs(self, root, cur, target, res):
        if not root:
            return
        if root.val == target:
            cur += 1
        else:
            cur = 1
        res[0] = max(res[0], cur)
        self.dfs(root.left, cur, root.val + 1, res)
        self.dfs(root.right, cur, root.val + 1, res)
        

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res)
        return res[0]
    
    def dfs(self, root, res):
        if not root:
            return 0
        
        curMax = 1
        left, right = self.dfs(root.left, res), self.dfs(root.right, res)

        if root.left and root.left.val == root.val + 1:
            curMax = max(curMax, left + 1)
        if root.right and root.right.val == root.val + 1:
            curMax = max(curMax, right + 1)
        
        res[0] = max(res[0], curMax)
        return curMax