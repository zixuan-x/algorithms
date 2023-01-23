# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        verticals = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, x = queue.popleft()
            verticals[x].append(node.val)
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))
        result = []
        for k in sorted(verticals):
            result.append(verticals[k])
        return result
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        verticals = defaultdict(list)
        left, right = 0, 0
        queue = deque([(root, 0)])
        while queue:
            node, x = queue.popleft()
            left = min(left, x)
            right = max(right, x)
            verticals[x].append(node.val)
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))
        result = []
        for x in range(left, right + 1):
            if x in verticals:
                result.append(verticals[x])
        return result
        

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        verticals = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            d = defaultdict(list)
            for _ in range(len(queue)):
                node, x = queue.popleft()
                d[x].append(node.val)
                if node.left:
                    queue.append((node.left, x - 1))
                if node.right:
                    queue.append((node.right, x + 1))
            for k in d:
                verticals[k].extend(d[k])
        result = []
        for k in sorted(verticals):
            result.append(verticals[k])
        return result