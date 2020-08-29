'''
面试中要问清楚除法处理的规则
recursion:
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t = tokens.pop()
        
        if t not in ['+', '-', '*', '/']:
            return int(t)
        
        right, left = self.evalRPN(tokens), self.evalRPN(tokens)
        
        if t == '+':
            return left + right
        if t == '-':
            return left - right
        if t == '*':
            return left * right
        if t == '/':
            return int(left / right)

'''
面试中要问清楚除法处理的规则
stack:
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                right, left = values.pop(), values.pop()
                result = 0
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    result = int(left / right)
                values.append(result)
            else:
                values.append(int(token))
        return values.pop()

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                right, left = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(float(left) / right))
        return stack.pop()