'''
max heap:
time: O(nlog(n-k) + klogk + klogn)
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        maxHeap = []
        kmax = []
        # O(nlog(n))
        for word in counter:
            # log(n - k)
            heappush(maxHeap, (-counter[word], word))
            if len(maxHeap) > len(counter) - k:
                # O(k)
                heappush(kmax, heappop(maxHeap))

        # O(klogk)
        result = []
        for _ in range(min(k, len(kmax))):
            result.append(heappop(kmax)[1])
        return result

'''
min heap:
'''
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)   
        
        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]