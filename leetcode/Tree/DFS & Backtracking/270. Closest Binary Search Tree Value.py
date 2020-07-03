# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res



class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = [root.val, abs(root.val - target)]
        self.dfs(root, target, res)
        return res[0]
    
    def dfs(self, root, target, res):
        if not root:
            return
        
        if abs(root.val - target) < res[1]:
            res[0] = root.val
            res[1] = abs(root.val - target)
            
        if target < root.val:
            self.dfs(root.left, target, res)
        else:
            self.dfs(root.right, target, res)
