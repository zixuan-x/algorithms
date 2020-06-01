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

''' 2. BFS - 1 '''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        cloned = {} # {index: Node}
        cloned[1] = Node(1)
        visited = set()
        
        queue = deque([node])
        while queue:
            node = queue.popleft()
            clonedNode = cloned[node.val]
            
            if node.val not in visited:
                visited.add(node.val)

                for neighbor in node.neighbors:
                    if neighbor.val not in cloned:
                        cloned[neighbor.val] = Node(neighbor.val)
                    clonedNode.neighbors.append(cloned[neighbor.val])
                    queue.append(neighbor)
        
        return cloned[1]

''' 2. BFS - 2 '''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        cloned = {} # {index: Node}
        cloned[1] = Node(1)
        visited = set([1])
        
        queue = deque([node])
        while queue:
            node = queue.popleft()
            clonedNode = cloned[node.val]
            
            for neighbor in node.neighbors:
                if neighbor.val not in cloned:
                    cloned[neighbor.val] = Node(neighbor.val)
                clonedNode.neighbors.append(cloned[neighbor.val])
                
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append(neighbor)
        
        return cloned[1]