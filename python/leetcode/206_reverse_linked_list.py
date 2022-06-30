# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Return if the length of the LinkedList is 0 or 1
        if not head or not head.next:
            return head
        
#         newHead = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
        
#         return newHead
        
        pre, cur = None, head
        
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
        return pre
        