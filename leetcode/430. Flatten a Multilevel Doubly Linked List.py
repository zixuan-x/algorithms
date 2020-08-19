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
        temp = head
        while temp:
            if temp.child:
                insertHead = self.flatten(temp.child)
                temp.child = None
                
                if temp.next:
                    insertTail = insertHead
                    while insertTail and insertTail.next:
                        insertTail = insertTail.next
                    # linking
                    next = temp.next
                    temp.next = insertHead
                    insertHead.prev = temp
                    insertTail.next = next
                    next.prev = insertTail
                    
                else:
                    temp.next = insertHead
                    insertHead.prev = temp
            temp = temp.next
        return head