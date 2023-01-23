'''
one list:

'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        self.bound = 0

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
        else:
            self.history[self.cur] = url
        self.bound = self.cur
        
        
    def back(self, steps: int) -> str:
        self.cur = max(self.cur - steps, 0)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, self.bound)
        return self.history[self.cur]


'''
two stacks: implemented using deque (can also use list)
[past] + cur + [future]

visit:
[past + cur] + url + []
- append cur to past
- cur = url
- future -> empty

back:
[past--] + past.pop() * min(steps, x) + [... + cur + future]
- pop min(steps, x) entries out from past
- appendleft cur and min(steps, x) - 1 elements to future

forware:
[past + cur + ...] + future.popleft() * min(steps, x) + [future--]
- popleft min(steps, x) entries out from future
- append cur and min(steps, x) - 1 elements to past
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.past = deque()
        self.cur = homepage
        self.future = deque()

    def visit(self, url: str) -> None:
        self.past.append(self.cur)
        self.cur = url
        if self.future:
            self.future = deque()
        
    def back(self, steps: int) -> str:
        self.future.appendleft(self.cur)
        for _ in range(min(steps, len(self.past))):
            self.future.appendleft(self.past.pop())
        self.cur = self.future.popleft()
        return self.cur

    def forward(self, steps: int) -> str:
        self.past.append(self.cur)
        for _ in range(min(steps, len(self.future))):
            self.past.append(self.future.popleft())
        self.cur = self.past.pop()
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)