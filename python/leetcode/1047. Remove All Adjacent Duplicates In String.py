'''
stack:
time: O(n)
space: O(n)
'''
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)

'''
two pointers:
time: O(n)
space: O(n)
'''
class Solution:
    def removeDuplicates(self, S: str) -> str:
        j = 0
        s = list(S)
        for i in range(len(s)):
            s[j] = s[i]
            if j > 0 and s[j] == s[j - 1]:
                j -= 2
            j += 1
        return ''.join(s[:j])