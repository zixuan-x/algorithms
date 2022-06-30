class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.valueIndexes = {}  # {value: index}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.valueIndexes:
            return False
        else:
            self.valueIndexes[val] = len(self.elements)
            self.elements.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.valueIndexes:
            return False
        else:    
            index = self.valueIndexes[val]
            value = self.elements[-1]
            
            self.elements[index] = value
            self.valueIndexes[value] = index
            
            self.elements.pop()
            del self.valueIndexes[val]

            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.elements[random.randint(0, len(self.elements) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()