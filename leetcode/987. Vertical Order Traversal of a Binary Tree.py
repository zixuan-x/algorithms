# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        verticals = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            level = defaultdict(list)
            for _ in range(len(queue)):
                node, x = queue.popleft()
                level[x].append(node.val)
                if node.left:
                    queue.append((node.left, x - 1))
                if node.right:
                    queue.append((node.right, x + 1))
            for k in level:
                verticals[k].extend(sorted(level[k]))
        result = []
        for x in sorted(verticals):
            result.append(verticals[x])
        return result
                
            