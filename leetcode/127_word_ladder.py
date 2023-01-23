from collections import defaultdict, deque
import string

'''双向BFS，只用两个set'''
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

'''双向BFS，用两个set和两个queue'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        words.add(beginWord)
        
        if endWord not in words:
            return 0
        
        s1, s2 = set(), set()
        q1, q2 = deque([beginWord]), deque([endWord])
        levels = 0
        while q1 or q2:
            if len(s1) > len(s2):
                s1, s2 = s2, s1
                q1, q2 = q2, q1
            levels += 1
            levelSize = len(q1)
            for i in range(levelSize):
                word = q1.popleft()
                if word not in s1:
                    if word in s2:
                        return levels - 1
                    s1.add(word)
                    for neighbor in self.getNeighbors(word, words):
                        q1.append(neighbor)
        return 0
                
        
        
    def getNeighbors(self, word, words):
        neighbors = []
        for i in range(len(word)):
            for j in range(97, 97 + 26):
                newWord = word[:i] + chr(j) + word[i+1:]
                if newWord in words and newWord != word:
                    neighbors.append(newWord)
        return neighbors

'''BFS'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        visited = set()
        levels = 1
        
        # bfs
        queue = deque([beginWord])
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

''''''
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
        queue = deque([beginWord])
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
        
''''''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge cases
        if beginWord == endWord: return 1
        wordList = set(wordList + [beginWord])
        if endWord not in wordList: return 0
        
        # build graph: {word: [words]}
        graph = self.buildGraph(wordList)
        
        # BFS
        visited = set([beginWord])
        level = 1
        queue = deque([beginWord])
        while queue:
            level += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                word = queue.popleft()
                for neighbor in graph[word]:
                    if neighbor not in visited:
                        if neighbor == endWord: return level
                        visited.add(neighbor)
                        queue.append(neighbor)
        return 0
    
    def buildGraph(self, wordList):
        graph = defaultdict(list)
        for word in wordList:
            graph[word] += self.findNeighbors(word, wordList)
        return graph
    
    def findNeighbors(self, word, wordList):
        neighbors = []
        for i in range(len(word)):
            for j in range(97, 97 + 26):
                newWord = word[:i] + chr(j) + word[i + 1:]
                if newWord in wordList:
                    neighbors.append(newWord)
        return neighbors