class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElement(head: Node, val: int) -> Node:
    if not head:
        return head
    
    newHead = removeElement(head.next, val)

    if head.val == val:
        return newHead
    else:
        head.next = newHead
        return head