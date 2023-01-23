'''
Intuition
If a string have occurrences x times,
any of its substring must appear at least x times.

There must be a substring of length minSize, that has the most occurrences.
So that we just need to count the occurrences of all substring with length minSize.


Explanation
Find the maximum occurrences of all substrings with length k = minSize


Complexity
time: O(n * minSize)
space: O(n * minSize)
'''
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # O(n * minSize)
        counter = Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        # O(n * minSize + n)
        return max([counter[sub] for sub in counter if len(set(sub)) <= maxLetters] + [0])

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            counter[sub] += 1
        result = 0
        for sub in counter:
            if len(set(sub)) <= maxLetters:
                result = max(result, counter[sub])
        return result