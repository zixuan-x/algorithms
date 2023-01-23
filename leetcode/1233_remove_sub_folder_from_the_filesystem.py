class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + '/'):
                res.append(str(path))
        return res