class Solution:
    def alienOrder(self, words: List[str]) -> str:
        sortedOrder = []
        
        # build graph -> adjacency list: char -> [char]
        success, graph, inDegree = self.buildGraph(words)
        
        if not success:
            return ''
        
        # build sources
        sources = deque()
        for key, value in inDegree.items():
            if value == 0:
                sources.append(key)
        
        # BFS
        while sources:
            c = sources.popleft()
            sortedOrder.append(c)
            for child in graph[c]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != len(inDegree):
            return ""
        return ''.join(sortedOrder)
            
            
    def buildGraph(self, words):
        graph = defaultdict(list)
        inDegree = {}
        for word in words:
            for c in word:
                inDegree[c] = 0
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if len(w1) > len(w2) and j == min(len(w1), len(w2)) - 1 and w1[j] == w2[j]:
                    return False, None, None
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    graph[c1].append(c2)
                    inDegree[c2] += 1
                    break
        
        return True, graph, inDegree