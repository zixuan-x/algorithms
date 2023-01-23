# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

''' 1. Backtracking '''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, [], res)
        return res
    
    
    def dfs(self, root, path, res):
        if not root:
            return
        
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append('->'.join(path))
    
        self.dfs(root.left, path, res)
        self.dfs(root.right, path, res)
        path.pop()


''' 2. BFS '''
def binaryTreePaths2(self, root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.left:
            queue.append((node.left, ls+str(node.val)+"->"))
        if node.right:
            queue.append((node.right, ls+str(node.val)+"->"))
    return res


''' 3. Backtracking with Stack '''
def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res