# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res)
        return res[0] - 1 if res[0] != 0 else 0
        
    def dfs(self, root, res) -> int:
        if not root:
            return 0
        else:
            left = self.dfs(root.left, res)
            right = self.dfs(root.right, res)
            res[0] = max(res[0], left + right + 1)
            return max(left, right) + 1