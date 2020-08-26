# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        self.search(root, sum, [], result)
        return result
    
    def search(self, root, sum, path, result):
        if not root:
            return
        
        if not root.left and not root.right:
            if root.val == sum:
                result.append(path + [root.val])
            return
        
        path.append(root.val)
        self.search(root.left, sum - root.val, path, result)
        self.search(root.right, sum - root.val, path, result)
        path.pop()