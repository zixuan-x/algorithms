'''
有的stack的题并不是要用到LIFO的性质
只不过是用到一个数组，然后恰好只需要在一端进行操作
这种题也可以用deque
因为不需要random index access
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        if not self.hasNext():
            return -1
        else:
            return self.stack.pop().getInteger()        
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            nestedInteger = self.stack.pop()
            self.stack.extend(nestedInteger.getList()[::-1])
        return len(self.stack) != 0
    
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())