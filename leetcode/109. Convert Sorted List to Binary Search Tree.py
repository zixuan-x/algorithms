# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
O(nlogn)
'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        slow, fast = head, head.next.next        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        mid = slow.next  
        slow.next = None
        
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
        

'''
O(n)
https://www.jiuzhang.com/solution/convert-sorted-list-to-binary-search-tree/
'''
class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        length = self.get_linked_list_length(head)
        root, next = self.convert(head, length)
        return root
    
    def get_linked_list_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
        
    def convert(self, head, length):
        if length == 0:
            return None, head
        
        left_root, middle = self.convert(head, length // 2)
        right_root, next = self.convert(middle.next, length - length // 2 - 1)
        
        root = TreeNode(middle.val)
        root.left = left_root
        root.right = right_root
        
        return root, next