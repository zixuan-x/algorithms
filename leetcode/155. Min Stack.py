class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = [float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]