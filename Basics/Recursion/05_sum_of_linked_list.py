class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def sum_of_linkedlist(head: Node):
    if not head:
        return 0

    return head.val + sum_of_linkedlist(head.next)

node = Node(1)
node.next = Node(2)
print(sum_of_linkedlist(node))