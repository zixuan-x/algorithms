# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1
        else:
            return min(left, right) + 1