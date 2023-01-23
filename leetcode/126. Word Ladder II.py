from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        distance = {} # {word: distance from endWord}
        wordSet = set(wordList + [beginWord])
        self.breathFristSearch(endWord, wordSet, distance)
        if beginWord not in distance:
            return []
        results = []
        self.depthFristSearch(beginWord, wordSet, [beginWord], distance, results)
        return results
        
    def breathFristSearch(self, endWord, wordSet, distance):
        distance[endWord] = 0
        queue = deque([endWord])
        while queue:
            word = queue.popleft()
            for neighbor in self.getNeighbors(word, wordSet):
                if neighbor not in distance:
                    distance[neighbor] = distance[word] + 1
                    queue.append(neighbor)
        
    def depthFristSearch(self, word, wordSet, path, distance, results):
        if distance[word] == 0:
            results.append(path[:])
            return
        
        for neighbor in self.getNeighbors(word, wordSet):
            if distance[neighbor] != distance[word] - 1:
                continue
            path.append(neighbor)
            self.depthFristSearch(neighbor, wordSet, path, distance, results)
            path.pop()       
    
    def getNeighbors(self, word, wordSet):
        neighbors = []
        for i in range(len(word)):
            for c in range(97, 97 + 26):
                newWord = word[:i] + chr(c) + word[i + 1:]
                if newWord != word and newWord in wordSet:
                    neighbors.append(newWord)
        return neighbors



class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        distance = {} # {word: distance from endWord}
        wordSet = set(wordList + [beginWord])
        self.breathFristSearch(endWord, wordSet, distance)
        if beginWord not in distance:
            return []
        results = []
        self.depthFristSearch(beginWord, wordSet, [beginWord], distance, results)
        return results
        
    def breathFristSearch(self, endWord, wordSet, distance):
        level = 0
        queue = deque([endWord])
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                word = queue.popleft()
                if word in distance:
                    continue
                distance[word] = level
                for neighbor in self.getNeighbors(word, wordSet):
                    queue.append(neighbor)
            level += 1
        
    def depthFristSearch(self, word, wordSet, path, distance, results):
        if distance[word] == 0:
            results.append(path[:])
            return
        
        for neighbor in self.getNeighbors(word, wordSet):
            if distance[neighbor] != distance[word] - 1:
                continue
            path.append(neighbor)
            self.depthFristSearch(neighbor, wordSet, path, distance, results)
            path.pop()       
    
    def getNeighbors(self, word, wordSet):
        neighbors = []
        for i in range(len(word)):
            for c in range(97, 97 + 26):
                newWord = word[:i] + chr(c) + word[i + 1:]
                if newWord != word and newWord in wordSet:
                    neighbors.append(newWord)
        return neighbors

