"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
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