'''
brute force:
1. convert transactions list to a list of Transaction objects
2. sort the list by their time
3. for -> list:
    1. if amount > 1000: add it
    2. for -> remaining list:
        1. if condition 2, add it

'''

class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # O(n)
        transactions = [Transaction(*t.split(',')) for t in transactions]
        
        # O(nlogn)
        transactions.sort(key=lambda t: t.time)
        invalids = set()
        
        # O(n ^ 2)
        for i in range(len(transactions)):
            t1 = transactions[i]
            if t1.amount > 1000:
                invalids.add(f'{t1.name},{t1.time},{t1.amount},{t1.city}')
            for j in range(i + 1, len(transactions)):
                t2 = transactions[j]
                if t2.name == t1.name and t2.time - t1.time <= 60 and t2.city != t1.city:
                    invalids.add(f'{t1.name},{t1.time},{t1.amount},{t1.city}')
                    invalids.add(f'{t2.name},{t2.time},{t2.amount},{t2.city}')
        
        # O(n)
        return list(invalids)
        
            