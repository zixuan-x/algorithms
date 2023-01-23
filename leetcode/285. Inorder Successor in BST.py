# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        node, succ = root, None
        while node:
            if p.val < node.val:
                succ = node
                node = node.left
            else:
                node = node.right
        return succ

''' Successor '''
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root

''' Predecessor '''
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root.val >= p.val:
            return self.inorderSuccessor(root.left, p)
        else:
            left = self.inorderSuccessor(root.right, p)
            return left if left else root