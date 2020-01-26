class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElment(head: Node, val: int):
    if not head:
        return head
    
    