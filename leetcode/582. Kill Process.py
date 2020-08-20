class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(list)
        for i in range(len(pid)):
            children[ppid[i]].append(pid[i])
        
        dead = [kill]
        queue = deque([kill])
        while queue:
            id = queue.popleft()
            for child in children[id]:
                dead.append(child)
                queue.append(child)
        return dead
        
        
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = {}
        for i in range(len(ppid)):
            tree[ppid[i]] = tree.get(ppid[i], [])
            tree[ppid[i]].append(pid[i])
        res = []
        queue = [kill]
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            queue += tree.get(cur, [])
        return res