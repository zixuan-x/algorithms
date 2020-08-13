# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
reverse linked list
time: O(m + n + max(m, n) + max(m + n) + 1) = O(m + n)
space: O(1)
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        dummy = ListNode(-1)
        prev = dummy
        carry = 0
        first, second = l1, l2
        while first or second:
            sum = carry
            carry = 0
            if first:
                sum += first.val
                first = first.next
            if second:
                sum += second.val
                second = second.next
            if sum >= 10:
                sum = sum % 10
                carry = 1
            prev.next = ListNode(sum)
            prev = prev.next
            
        if carry:
            prev.next = ListNode(1)
            prev = prev.next
            
        return self.reverse(dummy.next)
            
    def reverse(self, head):
        if not head or not head.next:
            return head
        
        prev, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

'''
stack:
time: O(m + n)
space: O(m + n)
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        dummy = ListNode(-1)
        carry = 0
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            carry, val = divmod(carry, 10)
            dummy.next = ListNode(val, dummy.next)
        return dummy.next