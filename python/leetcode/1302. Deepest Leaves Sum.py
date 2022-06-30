# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1. BFS
'''
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        result = 0
        while queue:
            levelSize = len(queue)
            result = 0
            for _ in range(levelSize):
                node = queue.popleft()
                result += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return result

'''
2. DFS (only checks leaf nodes)
'''
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = [0]
        maxDepth = [0]
        self.search(root, 1, maxDepth, result)
        return result[0]
        
    def search(self, root, curDepth, maxDepth, result):
        if not root:
            return
        
        if not root.left and not root.right:
            if curDepth > maxDepth[0]:
                maxDepth[0] = curDepth
                result[0] = root.val
            elif curDepth == maxDepth[0]:
                result[0] += root.val
            else:
                return
        
        self.search(root.left, curDepth + 1, maxDepth, result)
        self.search(root.right, curDepth + 1, maxDepth, result)


'''
3. DFS (checks every node)
'''
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = [0]
        maxDepth = [0]
        self.search(root, 1, maxDepth, result)
        return result[0]
        
    def search(self, root, curDepth, maxDepth, result):
        if not root:
            return
        
        if curDepth > maxDepth[0]:
            maxDepth[0] = curDepth
            result[0] = root.val
        elif curDepth == maxDepth[0]:
            result[0] += root.val
        
        self.search(root.left, curDepth + 1, maxDepth, result)
        self.search(root.right, curDepth + 1, maxDepth, result)