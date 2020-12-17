"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
[2:55] start
[3:04] solved (werid return type)
my solution is using O(n) space
A better solution use constant space by utilizing existing next pointer.
Recursive way? Worth thinking about.
"""

'''
1. BFS with level
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque([root])
        while queue:
            prev = None
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if prev: prev.next = node
                prev = node
        return root


'''
2. BFS without level
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if queue and queue[0][1] == level:
                node.next = queue[0][0]
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))
        return root


'''
3. DFS (This solution only works for perfect binary tree)
Note: This is a perfect binary tree
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # if root.right:  # This condition checks if there's next level, both left and right works
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root
                
        
            
        