# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []
        for i in range(len(lists)):
            l = lists[i]
            if l:
                heappush(minHeap, (l.val, i, l.next))
        
        dummy = ListNode(-1)
        prev = dummy
        while minHeap:
            val, i, l = heappop(minHeap)
            prev.next = ListNode(val)
            prev = prev.next
            if l:
                heappush(minHeap, (l.val, i, l.next))
        
        return dummy.next
