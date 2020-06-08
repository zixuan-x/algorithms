"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    """
    [2:55] start
    [3:04] solved (werid return type)
    my solution is using O(n) space
    A better solution use constant space by utilizing existing next pointer.
    Recursive way? Worth thinking about.
    """
    def connect(self, root: 'Node') -> 'Node':
        # res = []
        if not root:
            return root #res
        queue = collections.deque([root])
        while queue:
            levelSize = len(queue)
            prev = None
            for i in range(levelSize):
                cur = queue.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                # res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            # res.append('#')
        return root
        # return res
                
                
        
            
        