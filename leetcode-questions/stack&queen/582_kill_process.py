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