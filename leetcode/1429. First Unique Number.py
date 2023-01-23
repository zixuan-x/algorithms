class Node:
    def __init__(self, val):
        self.val = val 
        self.perv = None
        self.next = None

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.head = Node(-1)
        self.head.next = self.head
        self.head.prev = self.head
        self.seen = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.head.next != self.head:
            return self.head.next.val
        return -1
        
    def add(self, value: int) -> None:
        if value in self.seen:
            node = self.seen[value]
            if node:
                prev, next = node.prev, node.next
                prev.next = next
                next.prev = prev
                self.seen[value] = None
        else:
            node = Node(value)
            self.seen[value] = node
            node.prev = self.head.prev
            node.next = self.head
            node.prev.next = node
            node.next.prev = node  

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.seen = set()
        self.unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # for n in self.unique.keys():
        for n in self.unique:
            return n
        return -1
        # return next(iter(self.unique.keys()), -1)
        # return next(iter(self.unique), -1)

    def add(self, value: int) -> None:
        if value in self.seen:
            if value in self.unique:
                del self.unique[value]
        else:
            self.seen.add(value)
            self.unique[value] = None
        

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.seen = set()
        self.unique = deque()
        self.uniqueSet = set()
        for n in nums:
            if n not in self.seen:
                self.seen.add(n)
                self.uniqueSet.add(n)
                self.unique.append(n)
            else:
                if n in self.uniqueSet:
                    self.uniqueSet.remove(n)

    def showFirstUnique(self) -> int:
        while self.unique and self.unique[0] not in self.uniqueSet:
            self.unique.popleft()
        return self.unique[0] if self.unique else -1
        

    def add(self, value: int) -> None:
        if value in self.seen:
            if value in self.uniqueSet:
                self.uniqueSet.remove(value)
        else:
            self.seen.add(value)
            self.uniqueSet.add(value)
            self.unique.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)