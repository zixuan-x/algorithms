# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        mid = preorder[0]
        i = 0
        while i < len(inorder) and inorder[i] != mid:
            i += 1
        
        root = TreeNode(mid)
        root.left = self.buildTree(preorder[1:1+i], inorder[:i])
        root.right = self.buildTree(preorder[1+i:], inorder[i+1:])
        
        return root
        

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, inorder, 0, 0, len(inorder) - 1)
        
    def helper(self, preorder, inorder, preStart, inStart, inEnd):
        if preStart >= len(preorder) or inStart > inEnd:
            return None
        
        mid = preorder[preStart]
        i = inStart
        while i <= inEnd and inorder[i] != mid:
            i += 1
        
        root = ListNode(mid)
        root.left = self.helper(preorder, inorder, preStart + 1, inStart, i - 1)
        root.right = self.helper(preorder, inorder, preStart + i - inStart + 1, i + 1, inEnd)
        return root
        