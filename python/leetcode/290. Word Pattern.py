class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        
        dic = {}  # {char: word}
        visited = set()
        
        for i in range(len(words)):
            char, word = pattern[i], words[i]
            if char not in dic:
                if word in visited:
                    return False
                dic[char] = word
                visited.add(word)
            else:
                if dic[char] != word:
                    return False
                
        return True