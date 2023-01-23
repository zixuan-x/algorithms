# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        predecessors = []
        successors = []
        res = []
        
        self.inorder(root, target, predecessors, False)
        self.inorder(root, target, successors, True)
        
        for _ in range(k):
            if not predecessors:
                res.append(successors.pop())
            elif not successors:
                res.append(predecessors.pop())
            elif abs(successors[-1] - target) < abs(predecessors[-1] - target):
                res.append(successors.pop())
            else:
                res.append(predecessors.pop())
                
        return res
        
    
    def inorder(self, root, target, stack, reverse):
        if not root: return
        
        self.inorder(root.right if reverse else root.left, target, stack, reverse)
        
        if (reverse and root.val <= target) or (not reverse and root.val > target):
            return
        stack.append(root.val)
        
        self.inorder(root.left if reverse else root.right, target, stack, reverse)
        