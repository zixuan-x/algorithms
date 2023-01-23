# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45740/Summary-of-preorder-inorder-postorder-four-traversal-ways-for-each
# 1. Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# 2. Iterative with Stack
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res
