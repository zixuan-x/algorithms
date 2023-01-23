'''
Python Cheating Solution
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = sorted(list(s), key=lambda x: (c[x], x), reverse=True)
        return ''.join(s)

'''
bucket sort: (frequency bucket)
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        
        frequencies = defaultdict(list)  # {frequency: []}
        for char, times in c.items():
            frequencies[times] += [char] * times
        
        result = []
        for times in range(len(s), 0, -1):
            if times in frequencies:
                result += frequencies[times]
        return ''.join(result)

'''
heap
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        
        maxHeap = []
        for char, times in c.items():
            heappush(maxHeap, (-times, char))
        
        result = []
        while maxHeap:
            times, char = heappop(maxHeap)
            times = -times
            result += [char] * times
        return ''.join(result)
