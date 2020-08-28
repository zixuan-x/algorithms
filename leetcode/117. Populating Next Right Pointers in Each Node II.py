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
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        nextLevel = ListNode(-1)
        prev = nextLevel
        while cur:
            if cur.left:
                prev.next = cur.left
                prev = prev.next
            if cur.right:
                prev.next = cur.right
                prev = prev.next
            cur = cur.next
            if not cur:
                cur = nextLevel.next
                nextLevel.next = None
                prev = nextLevel
        return root

        
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        nextLevel = None
        cur = root
        prev = None
        while cur or nextLevel:
            if not cur:
                cur = nextLevel
                nextLevel = None
                prev = None
            
            if cur.left:
                if not nextLevel:
                    nextLevel = cur.left
                if prev:
                    prev.next = cur.left
                prev = cur.left
                
            if cur.right:
                if not nextLevel:
                    nextLevel = cur.right
                if prev:
                    prev.next = cur.right
                prev = cur.right
                
            cur = cur.next
        
        return root
        
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        res = root
        temp = ListNode(-1)
        cur = temp
        while root:
            if root.left:
                cur.next = root.left
                cur = cur.next
            if root.right:
                cur.next = root.right
                cur = cur.next
            root = root.next
        self.connect(temp.next)
        return res