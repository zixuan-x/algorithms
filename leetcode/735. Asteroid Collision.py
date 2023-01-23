class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if (not stack) or asteroid > 0 or stack[-1] < 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == abs(asteroid):
                    stack.pop()
        return stack
                

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if (not stack) or (asteroid * stack[-1] > 0) or (asteroid > 0 and stack[-1] < 0):
                stack.append(asteroid)
            else:
                while True:
                    if not stack or stack[-1] < 0:
                        stack.append(asteroid)
                        break
                    elif abs(asteroid) == abs(stack[-1]):
                        stack.pop()
                        break
                    elif abs(asteroid) > abs(stack[-1]):
                        stack.pop()
                    else:
                        break
        return stack
