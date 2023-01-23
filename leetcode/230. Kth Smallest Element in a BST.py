# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

''' 1. DFS '''
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
        num = [0]
        self.dfs(root, num, [0], k)
        return num[0]
        
    def dfs(self, root, num, count, k):
        if not root:
            return
        
        self.dfs(root.left, num, count, k)
        
        count[0] += 1
        if count[0] == k:
            num[0] = root.val
            return  
        
        self.dfs(root.right, num, count, k)

''' 2. DFS with Stack'''
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        count = 0
        
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                count += 1
                if count == k:
                    return cur.val
                cur = cur.right
        
        return -1
        