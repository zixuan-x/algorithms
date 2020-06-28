# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, [], res)
        return res
    
    def dfs(self, root, sum, path, res):
        if not root:
            return
        
        path.append(root.val)
        if not root.left and not root.right and root.val == sum:
            res.append(path[:])
            # path.pop()
            # return
        
        self.dfs(root.left, sum - root.val, path, res)
        self.dfs(root.right, sum - root.val, path, res)
        
        path.pop()
            