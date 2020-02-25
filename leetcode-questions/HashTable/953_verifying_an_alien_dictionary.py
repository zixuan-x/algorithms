class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # m = {c: i for i, c in enumerate(order)}
        # words = [[m[c] for c in w] for w in words]
        # return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
        
        alphabet = {}
        for i, s in enumerate(order):
            alphabet[s] = i
        
        for i in range(len(words) - 1):
            if not self.smaller(words[i], words[i + 1], alphabet):
                return False
        
        return True
    
    def smaller(self, s1, s2, alphabet):
        n = min(len(s1), len(s2))
        
        for i in range(n):
            if alphabet[s1[i]] < alphabet[s2[i]]:
                return True
            elif alphabet[s1[i]] > alphabet[s2[i]]:
                return False
            else:
                pass
        
        return len(s1) <= len(s2)