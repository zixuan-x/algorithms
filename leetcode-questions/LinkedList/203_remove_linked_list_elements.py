# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
#         if head == None:
#             return head
        
#         newHead = self.removeElements(head.next, val)
        
#         if head.val == val:
#             return newHead
#         else:
#             head.next = newHead
#             return head
        dummyNode = ListNode(-1)
        dummyNode.next = head
        pre = dummyNode
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummyNode.next