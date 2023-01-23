class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None] * 1000
        self.size = 1000
        self.dummy = ListNode(-1, -1)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        self.dummy.next = self.arr[index]
        pre = self.dummy
        while pre.next:
            if pre.next.key == key:
                pre.next.value = value
                return
            pre = pre.next
        pre.next = ListNode(key, value)
        self.arr[index] = self.dummy.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        self.dummy.next = self.arr[index]
        pre = self.dummy
        while pre.next:
            if pre.next.key == key:
                return pre.next.value
            pre = pre.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        self.dummy.next = self.arr[index]
        pre = self.dummy
        while pre.next:
            if pre.next.key == key:
                pre.next = pre.next.next
                break
            pre = pre.next
        self.arr[index] = self.dummy.next
        print(self.arr[index])

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)