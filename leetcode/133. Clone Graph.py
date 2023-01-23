from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

''' 1. DFS '''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs(node, {})
        
    def dfs(self, node, created):
        if not node:
            return node
        newNode = Node(node.val)
        created[node.val] = newNode
        
        for neighbor in node.neighbors:
            if neighbor.val not in created:
                newNeighbor = self.dfs(neighbor, created)
                newNode.neighbors.append(newNeighbor)
                created[newNeighbor.val] = newNeighbor
            else:
                newNode.neighbors.append(created[neighbor.val])
                
        return newNode

''' 2. BFS '''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        cloned = {node: Node(node.val)}
        visited = set([node])
        queue = deque([node])
        while queue:
            original = queue.popleft()
            clone = cloned[original]
            for neighbor in original.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                clone.neighbors.append(cloned[neighbor])
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return cloned[node]