# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# preorder == reversed postorder
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root, None)
        

    def dfs(self, root, tailHead):
        if not root:
            return tailHead
        
        tailHead = self.dfs(root.right, tailHead)
        tailHead = self.dfs(root.left, tailHead)
        
        root.right = tailHead
        root.left = None
        return root


class Solution:
    """
    postorder traversal from right to left
    use prev to connect nodes together
    remember to set root.left to None
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

