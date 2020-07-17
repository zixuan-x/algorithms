# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        
        small, large = ListNode(-1), ListNode(-1)
        s, l, cur = small, large, head
        while cur:
            if cur.val < x:
                s.next = cur
                s = s.next
            else:
                l.next = cur
                l = l.next
            cur = cur.next
        s.next = large.next
        l.next = None
        return small.next