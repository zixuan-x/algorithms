"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        mapping = {}
        orig = head
        while orig:
            mapping[orig] = Node(orig.val)
            orig = orig.next
        orig = head
        while orig:
            mapping[orig].next = mapping[orig.next] if orig.next else None
            mapping[orig].random = mapping[orig.random] if orig.random else None
            orig = orig.next
        return mapping[head]