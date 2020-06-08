# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, [], res)
        return res
        
    def dfs(self, root, cur, res):
        if not root:
            return
        elif not root.left and not root.right:
            cur.append(str(root.val))
            res.append(''.join(cur))
            cur.pop()
            return
        else:
            cur.append(str(root.val) + '->')
            self.dfs(root.left, cur, res)
            self.dfs(root.right, cur, res)
            cur.pop()