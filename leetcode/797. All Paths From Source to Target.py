class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        self.search(graph, 0, [], result)
        return result
        
    def search(self, graph, index, path, result):
        if index == len(graph) - 1:
            result.append(path + [index])
            return 
        
        path.append(index)
        for neighbor in graph[index]:
            self.search(graph, neighbor, path, result)
        path.pop()