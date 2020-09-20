class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        valueToIndex = defaultdict(list)
        for i, v in enumerate(B):
            valueToIndex[v].append(i)
        result = []
        for v in A:
            result.append(valueToIndex[v].pop())
        return result            