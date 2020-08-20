

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