class StockSpanner:

    def __init__(self):
        self.prices = []
        self.dp = []
        
    def next(self, price: int) -> int:
        length = len(self.dp)
        if length == 0 or price < self.prices[-1]:
            self.dp.append(1)
        else:
            i = length - 1
            while i >= 0 and self.prices[i] <= price:
                i -= self.dp[i]
            self.dp.append(length - i)
        self.prices.append(price)
        length += 1
        return self.dp[-1]

class StockSpanner:

    def __init__(self):
        self.stack = [] # [price, number], order by price DESC
        
    def next(self, price: int) -> int:
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res