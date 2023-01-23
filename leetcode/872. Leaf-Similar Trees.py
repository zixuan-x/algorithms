# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. Generate two lists (global variable) and compare them
'''
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        sequence1, sequence2 = [], []
        self.getLeafSequence(root1, sequence1)
        self.getLeafSequence(root2, sequence2)
        return sequence1 == sequence2
        
    def getLeafSequence(self, root, sequence):
        if not root:
            return
        
        if not root.left and not root.right:
            sequence.append(root.val)
            return
        
        self.getLeafSequence(root.left, sequence)
        self.getLeafSequence(root.right, sequence)
        

'''
2. Generate two lists (return value) and compare them
'''
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.getLeafSequence(root1) == self.getLeafSequence(root2)
        
    def getLeafSequence(self, root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        return self.getLeafSequence(root.left) + self.getLeafSequence(root.right)

'''
3. Compare without generating lists
'''