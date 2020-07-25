from collections import defaultdict, deque

'''
https://leetcode.com/problems/course-schedule-iv/discuss/660883/Clean-Python-3-topological-sort-and-set-O(P-*-N)
This problem is about check if 2 vertices are connected in directed graph.

n -> number of courses
p -> number of prerequisite pairs
q -> number of queries

time: O(n) + O(p) + O(n) + O(n * 1) + O(p * n) + O(q) = O(p * n)
space: O(n ^ 2) for all sets
'''
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]: 
        
        
        # initialization - O(n)
        graph = defaultdict(list)
        inDegree = {i: 0 for i in range(n)}
        precourses = defaultdict(set)
        
        # build graph - O(p)
        for parent, child in prerequisites:
            graph[parent].append(child)
            inDegree[child] += 1
            precourses[child].add(parent)
        
        # O(n)
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # Outer loop - O(n)
        while sources:
            parent = sources.popleft()
            
            # O(p) in total since we visit all edges
            for child in graph[parent]:
                precourses[child] |= precourses[parent] # O(n)
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        # O(q)
        # results = []
        # for parent, child in queries:
        #     results.append(parent in precourses[child])
        return [c1 in precourses[c2] for c1, c2 in queries]