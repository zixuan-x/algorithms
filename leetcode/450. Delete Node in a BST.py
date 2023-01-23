# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: # if root doesn't exist, just return it
            return root
        if root.val > key: # if key value is less than root value, find the node in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: # if key value is greater than root value, find the node in right subtree
            root.right= self.deleteNode(root.right, key)
        else: #if we found the node (root.value == key), start to delete it
            if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
                return root.left
            if not root.left: # if it has no left children, we delete the node then new root would be root.right
                return root.right
                   # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini # replace value
            root.right = self.deleteNode(root.right,root.val) # delete the minimum node in right subtree
        return root