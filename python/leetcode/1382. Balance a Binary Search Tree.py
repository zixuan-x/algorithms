# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.inorder(root)
        return self.toBST(nums, 0, len(nums) - 1)
        
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        
    def toBST(self, nums, left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.toBST(nums, left, mid - 1)
        root.right = self.toBST(nums, mid + 1, right)
        
        return root