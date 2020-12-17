from collections import defaultdict, deque

'''
Reconstruction means building a shortest common supersequence of the sequences in seqs
Note: sequence -> dependency -> topsort
'''
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph, inDegree = self.buildGraph(seqs)
        sortedOrder = []
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            if len(sources) > 1: return False
            num = sources.popleft()
            sortedOrder.append(num)
            for child in graph[num]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return sortedOrder == org and len(sortedOrder) == len(inDegree)
    
    def buildGraph(self, seqs):
        graph, inDegree = defaultdict(list), {}
        
        for seq in seqs:
            for num in seq:
                if num not in inDegree:
                    inDegree[num] = 0
        
        for seq in seqs:
            for i in range(len(seq) - 1):
                n1, n2 = seq[i], seq[i + 1]
                graph[n1].append(n2)
                inDegree[n2] += 1
        return graph, inDegree