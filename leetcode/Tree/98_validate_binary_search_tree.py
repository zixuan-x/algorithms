# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    [12:42] start
    use recursion, pass in left and righr boundary
    [12:46] solved
    """
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))
        
    def dfs(self, root, left, right):
        """
        (TreeNode, int, int) -> bool
        """
        if not root:
            return True
        elif root.val <= left or root.val >= right:
            return False
        else:
            return self.dfs(root.left, left, root.val) and self.dfs(root.right, root.val, right)
        
        