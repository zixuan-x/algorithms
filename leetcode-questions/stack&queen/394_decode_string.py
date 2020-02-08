class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        
        num_stack = []
        str_stack = [""]
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while s[i].isdigit():
                    i += 1
                num_stack.append(int(s[start:i]))
            elif s[i] == '[':
                i += 1
                temp = ""
                while s[i].isalpha():
                    temp += s[i]
                    i += 1
                str_stack.append(temp)
                
            elif s[i] == ']':
                temp = str_stack.pop() * num_stack.pop()
                str_stack.append(str_stack.pop() + temp)
                i += 1
            else:
                str_stack.append(str_stack.pop() + s[i])
                i += 1
        
        return str_stack.pop()
        