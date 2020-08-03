'''
1. 
'''
class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.head = Node(-1, -1)
        self.head.left = self.head
        self.head.right = self.head
        
        self.dic = {}  # {key: ListNode}

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.moveToHead(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.moveToHead(node)
        else:
            node = Node(key, value)
            self.dic[key] = node
            self.moveToHead(node)
            if self.size() > self.capacity:
                node_to_remove = self.head.left
                key_to_remove = node_to_remove.key
                self.removeNode(node_to_remove)
                self.removeKey(key_to_remove)
    
    def size(self) -> int:
        return len(self.dic)
    
    def moveToHead(self, node):
        if node.left and node.right:
            self.removeNode(node)

        node.left = self.head
        node.right = self.head.right

        node.left.right = node
        node.right.left = node
    
    def removeNode(self, node):
        node.left.right = node.right
        node.right.left = node.left
        
    def removeKey(self, key):
        self.dic.pop(key)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
2. 
'''
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # check if key is in d
        if key in self.d:
            # if is inside, get value, move to head
            node = self.d[key] 
            self.removeNode(node)
            self.addHead(node)
            return node.val
        # else return -1
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # check if key is in d
        if key in self.d:
            # if so update value
            node = self.d[key]
            node.val = value
            # move it to the head
            self.removeNode(node)
            self.addHead(node)
        # else create new entry in d
        else:
            node = Node(key, value)
            # add new node to the head & d
            self.addHead(node)
            self.d[key] = node
            # check capacity
            if len(self.d) > self.capacity:
                self.popTail()
    
    # remove the node at given 
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    # add the node at the head of the list
    def addHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        node.prev.next = node
    
    # remove the node at the tail of the list
    def popTail(self):
        node = self.tail.prev
        del self.d[node.key]
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)