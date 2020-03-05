import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordList:
            return 0
        
        levels = 0
        s1 = set([beginWord])
        s2 = set([endWord])
        wordSet.remove(endWord)
        
        while s1 and s2:
            levels += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            
            s = set()
            for word in s1:
                for i in range(len(word)):
                    for l in string.ascii_lowercase:
                        newWord = word[:i] + l + word[i + 1:]
                        if newWord in s2:
                            return levels + 1
                        if newWord in wordSet:
                            s.add(newWord)
                            wordSet.remove(newWord)
            s1 = s
        return 0

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        visited = set()
        levels = 1
        
        # bfs
        queue = collections.deque([beginWord])
        visited.add(beginWord)
        while queue:
            levelSize =len(queue)
            levels += 1
            for i in range(levelSize):
                cur = queue.popleft()
                neighbors = self.getNeighbors(cur, words)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        if neighbor == endWord:
                            return levels
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return 0
                
    
    def getNeighbors(self, word, words):
        neighbors = []
        for i in range(len(word)):
            for l in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[0:i] + l + word[i + 1:]
                if newWord in words:
                    neighbors.append(newWord)
        
        return neighbors

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build graph & visited
        g = {}
        wordList.append(beginWord)
        words = set(wordList)
        levels = 0
        
        chars = "abcdefghijklmnopqrstuvwxyz"
        for word in wordList:
            g[word] = []
            for i in range(len(word)):
                for l in chars:
                    newWord = word[0:i] + l + word[i + 1:]
                    if newWord in words:
                        g[word].append(newWord)
        
        visited = set()
        
        # queue & bfs
        queue = collections.deque([beginWord])
        while queue:
            levelSize = len(queue)
            levels += 1
            for i in range(levelSize):
                cur = queue.popleft()
                if cur == endWord:
                    return levels
                visited.add(cur)
                neighbors = g[cur]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return 0
        
            
        