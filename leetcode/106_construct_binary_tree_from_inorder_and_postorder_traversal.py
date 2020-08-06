# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    [1:15] start
    preorder/postorder -> root
    inorder -> left, right subtree
    inorder also tells us how many nodes are in the left, right subtree
    中途看了会剧。。。
    [1:21] continue
    subproblem is the same as the problem, so use divide and conquer
    How to divide postorder into half? 
    pop postorder everytime and go right before go left, 
        such that the right most element will always be the root
    [1:32] solved
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(inorder, postorder)
    
    def helper(self, inorder, postorder) -> TreeNode:
        if not inorder or not postorder:
            return None
        else:
            root = TreeNode(postorder[-1])
            rootIndex = inorder.index(root.val)
            
            root.left = self.helper(inorder[:rootIndex], postorder[:rootIndex])
            root.right = self.helper(inorder[rootIndex + 1:], postorder[rootIndex:-1])
            
            return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.helper(inorder, postorder)
        
    def helper(self, inorder, postorder) -> TreeNode:
        if not inorder or not postorder:
            return None
        else:
            root = TreeNode(postorder.pop())
            rootIndex = inorder.index(root.val)
            leftBoundary = rootIndex - 1 if rootIndex > 0 else -1
            root.right = self.helper(inorder[rootIndex + 1:], postorder)
            root.left = self.helper(inorder[:rootIndex], postorder)
            
            return root