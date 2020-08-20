# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        width = 0
        queue = deque([(1, root)])
        while queue:
            width = max(width, queue[-1][0] - queue[0][0] + 1)
            levelSize = len(queue)
            for _ in range(levelSize):
                id, node = queue.popleft()
                if node.left:
                    queue.append((id * 2, node.left))
                if node.right:
                    queue.append((id * 2 + 1, node.right))
        return width
        