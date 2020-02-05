# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 1. testing
        if not head or not head.next:
            return head
        
        # 2. halving
        pre, left, right = None, head, head
        while right and right.next:
            pre = left
            left = left.next
            right = right.next.next
        pre.next = None
        right = left
        left = head
        
        # 3. sorting
        left = self.sortList(left)
        right = self.sortList(right)
        
        # 4. combining
        result = ListNode(-1)
        cur = result
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
            
        cur.next = left if left else right
        
        return result.next
        