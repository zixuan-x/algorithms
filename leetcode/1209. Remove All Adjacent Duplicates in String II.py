'''
stack:
time: O(N)
space: O(N)
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append(c)
            else:
                stack.append(stack.pop() + c)
                if len(stack[-1]) == k:
                    stack.pop()
        return ''.join(stack)

    def removeDuplicates(self, s, k):
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

'''
two pointers:
time: O(n)
space: O(n)
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        j = 0
        s = list(s)
        count = [1] * len(s)
        for i in range(len(s)):
            s[j] = s[i]
            if j > 0 and s[j] == s[j - 1]:
                count[j] = count[j - 1] + 1
            else:
                count[j] = 1
            if count[j] == k:
                j -= k
            j += 1
        return ''.join(s[:j])

'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392867/C%2B%2B-3-approaches
brute force:
time: O(n * n / k)
space: 
'''
# string removeDuplicates(string s, int k) {
#   for (auto i = 1, cnt = 1; i < s.size(); ++i) {
#     if (s[i] != s[i - 1]) cnt = 1;
#     else if (++cnt == k)
#       return removeDuplicates(s.substr(0, i - k + 1) + s.substr(i + 1), k);
#   }
#   return s;
# }

# string removeDuplicates(string s, int k, bool replaced = true) {
#   while (replaced) {
#     replaced = false;
#     for (auto i = 1, cnt = 1; i < s.size() && !replaced; ++i) {
#       if (s[i] != s[i - 1]) cnt = 1;
#       else if (++cnt == k) {
#         s = s.substr(0, i - k + 1) + s.substr(i + 1);
#         replaced = true;
#       }
#     }
#   }
#   return s;
# }
