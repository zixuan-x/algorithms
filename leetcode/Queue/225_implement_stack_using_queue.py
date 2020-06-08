'''
There are two solutions cost O(n) and O(1) for different operations:

push: O(n), pop/top: O(1)
push: O(1), pop/top: O(n)
Time efficiency depends on operation frequency of push, pop, top:
if push>pop+top, second solution is better.
if push<pop+top, first solution is better.

And I feel, in most cases, push<pop+top.

除了下面的解法，也可以只用一个queue

Solution 1: 
    init - 1: self.queue & self.temp
    push - n: put into temp, then move all elements in queue to temp, then swap
    pop - 1: pop out the head of the queue
    top - 1: peek head of queue
    empty - 1: check if queue is empty

Solution 2:
    init - 1: self.queue & self.temp
    push - 1: put to the end of queue
    pop - n: move n - 1 elements to temp, then pop the last one, then swap
    top - n: move n - 1 elements to temp, peek, add last one to temp, then swap
    empty - 1: check if queue is empty
'''

'''Solution 1'''
from collections import deque

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.temp = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.temp.append(x)
        while self.queue:
            self.temp.append(self.queue.popleft())
        self.queue, self.temp = self.temp, self.queue
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return -1
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return -1
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

'''Solution 2'''
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.temp = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return -1
        size = len(self.queue)
        for _ in range(size - 1):
            self.temp.append(self.queue.popleft())
        res = self.queue.popleft()
        self.queue, self.temp = self.temp, self.queue
        return res
        
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return -1
        size = len(self.queue)
        for _ in range(size - 1):
            self.temp.append(self.queue.popleft())
        res = self.queue[0]
        self.temp.append(self.queue.popleft())
        self.queue, self.temp = self.temp, self.queue
        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0