from collections import Counter



'''Greedy Solution'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_count = max(value for key, value in counter.items())
        max_nums = sum(1 if value == max_count else 0 for key, value in counter.items())
        
        if max_nums > n:
            return len(tasks)
        
        slots = (n - max_nums + 1) * (max_count - 1)
        
        if len(tasks) - max_count * max_nums >= slots:
            return len(tasks)
        else:
            return len(tasks) + slots - (len(tasks) - max_count * max_nums)