# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        first = head
        second = slow.next
        slow.next = None
        
        pre, cur, next = None, second, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        second = pre
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True