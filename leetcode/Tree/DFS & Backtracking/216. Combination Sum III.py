class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        self.search(k, n, 1, [], combinations)
        return combinations
        
    def search(self, k, n, start, path, combinations):
        if start == 10 or k == 0 or n <= 0:
            if n == 0 and k == 0:
                combinations.append(path[:])
            return
        
        for i in range(start, 10):
            path.append(i)
            self.search(k - 1, n - i, i + 1, path, combinations)
            path.pop()