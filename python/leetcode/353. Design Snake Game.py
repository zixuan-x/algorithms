'''
use row and column instead of x and y
'''
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.rows = height
        self.cols = width
        self.food = food
        self.snakeSet = set([(0, 0)])
        self.snake = deque([(0, 0)])
        self.nextfood = 0
        self.head = (0, 0)

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # move one unit
        r, c= self.head
        if direction == 'L':
            c -= 1
        elif direction == 'R':
            c += 1
        elif direction == 'U':
            r -= 1
        else: # 'D'
            r += 1
            
        # if new head is not valid
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return -1
        
        # if food is not avaliable
        if self.nextfood == len(self.food):
            tail = self.snake.popleft()
            self.snakeSet.remove(tail)
        else:
        # if food is available
            fr, fc = self.food[self.nextfood]  # get position of food
            # if equal, move to next food
            if (r, c) == (fr, fc):
                self.nextfood += 1
            else:
                # remove tail if not equal
                tail = self.snake.popleft()
                self.snakeSet.remove(tail)
        
        if (r, c) in self.snakeSet:
            return -1
        
        # if valid, update snake
        self.head = (r, c)
        self.snake.append((r, c))
        self.snakeSet.add((r, c))
        
        return len(self.snake) - 1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)