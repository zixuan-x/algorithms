class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        combinations = []
        digit_to_letter = { # {digit: [letters]}
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        } 
        self.dfs(digits, 0, [], combinations, digit_to_letter)
        return combinations
    
    def dfs(self, digits, index, path, combinations, digit_to_letter):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        
        for letter in digit_to_letter[int(digits[index])]:
            path.append(letter)
            self.dfs(digits, index + 1, path, combinations, digit_to_letter)
            path.pop()
            