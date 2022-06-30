class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            key = ','.join(map(str, counter))
            mapping[key].append(s)
        result = []
        for key in mapping:
            result.append(mapping[key])
        return result