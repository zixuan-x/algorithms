''' 1. Recursive '''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

''' 2. Iterative with Stack '''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        
        return res[::-1]
