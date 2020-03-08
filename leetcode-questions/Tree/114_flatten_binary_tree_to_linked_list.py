# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    [1:54] start
    postorder traversal from right to left
    又去看剧了
    [2:45] continue
    use prev to connect nodes together
    remember to set root.left to None
    [2:49]
    """
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root, [None])
        
    def dfs(self, root, prev):
        if not root:
            return
        else:
            self.dfs(root.right, prev)
            self.dfs(root.left, prev)
            root.right = prev[0]
            root.left = None
            prev[0] = root