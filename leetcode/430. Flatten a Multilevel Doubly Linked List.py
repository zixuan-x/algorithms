"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        self.flattenHelper(head)
        return head
    
    def flattenHelper(self, head) -> ('Node', 'Node'):
        if not head:
            return head
        
        cur, prev = head, None
        while cur:
            if cur.child:
                # store before flatten the list
                childHead = cur.child
                next = cur.next
                # flatten
                childTail = self.flattenHelper(cur.child)
                # connect
                cur.child = None
                cur.next = childHead
                childHead.prev = cur
                childTail.next = next
                if next:
                    next.prev = childTail
                prev = childTail
                cur = next
            else:
                prev = cur
                cur = cur.next
        return prev

