''' 1. '''
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        if self.prune(root) == 0:
            return None
        return root
        
    def prune(self, root) -> int:
        if not root:
            return 0
        
        left = self.prune(root.left) 
        if left == 0:
            root.left = None
        
        right = self.prune(root.right) 
        if right == 0:
            root.right = None
            
        return int(root.val == 1) + left + right

''' 2. '''
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right and not root.val:
            return None
        return root