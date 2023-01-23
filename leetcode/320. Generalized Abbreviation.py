class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if not word:
            return [""]
        result = []
        self.search(word, 0, 0, [], result)
        return result 
        
    def search(self, word, index, count, path, result):
        if index == len(word):
            if count > 0:
                path.append(str(count))
            result.append(''.join(path))
            if count > 0:
                path.pop()
            return
        
        # abbreviate
        self.search(word, index + 1, count + 1, path, result)
        
        # don't abbreviate
        if count > 0:
            path.append(str(count))
        
        path.append(word[index])
        self.search(word, index + 1, 0, path, result)
        path.pop()
        
        if count > 0:
            path.pop()