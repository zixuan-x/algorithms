from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, inDegree, error = self.buildGraph(words)
        if error: return ''
        
        sortedOrder = []
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            c = sources.popleft()
            sortedOrder.append(c)
            for child in graph[c]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != len(inDegree):
            return ''
        return ''.join(sortedOrder)
        
    
    def buildGraph(self, words):
        graph, inDegree = defaultdict(list), {}
        for word in words:
            for c in word:
                if c not in inDegree:
                    inDegree[c] = 0
                    
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    graph[first[j]].append(second[j])
                    inDegree[second[j]] += 1
                    break
                if j == min(len(first), len(second)) - 1 and len(first) > len(second):
                    return None, None, True
        
        return graph, inDegree, False