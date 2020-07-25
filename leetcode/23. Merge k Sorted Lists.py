# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        minHeap = []
        # push the first node of all lists into minHeap
        index = 0
        for i in range(len(lists)):
            l = lists[i]
            if l:
                heappush(minHeap, (l.val, index, l))
                index += 1
        
        dummy = ListNode(-1)
        pre = dummy
        while minHeap:
            _, _, l = heappop(minHeap)
            pre.next = l
            pre = pre.next
            if l.next:
                heappush(minHeap, (l.next.val, index, l.next))
                index += 1
        return dummy.next
