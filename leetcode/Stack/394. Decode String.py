class Solution:
    def decodeString(self, s: str) -> str:
        repeat_stack = []
        str_stack = []
        cur_str = ''
        cur_num = 0
        
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                repeat_stack.append(int(cur_num))
                str_stack.append(cur_str)
                cur_str = ''
                cur_num = 0
            elif c == ']':
                cur_str = str_stack.pop() + cur_str * repeat_stack.pop()
            else:
                cur_str += c
        
        return cur_str