# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/balanced-binary-tree/discuss/35691/The-bottom-up-O(N)-solution-would-be-better

''' 1. O(n ^ 2) '''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self, root):
        if not root:
            return 0
        
        return max(self.depth(root.left), self.depth(root.right)) + 1


''' 2. O(n) with Global Variable'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        res = [True]
        self.depth(root, res)
        return res[0]
        
    def depth(self, root, res):
        if not root:
            return 0
        
        left = self.depth(root.left, res)
        right = self.depth(root.right, res)
        
        if abs(left - right) > 1:
            res[0] = False
        
        return max(left, right) + 1

''' 3. O(n) with -1 as return value '''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.depth(root) != -1
        
    def depth(self, root):
        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        if left == -1 or right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1