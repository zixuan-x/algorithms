'''The idea is to use a single list of fixed size k and keep the references to front and rear indices in the array. 
Since we don't deal with any of the memory allocation/deletion/pointer manipulation, this solution is very fast IMO

Note：array size选为k + 1, 留个空位可以减少很多edge cases
    如果size是k，front和rear一开始等于-1，enqueue第一个元素的时候必须把front也变成0，
    否则调用Front()函数时访问的是index -1而不是0，
    所以要么在enqueue要么Front函数里面多加一个if/else判断。
'''
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.array = [0] * (k + 1)
        self.front = 0
        self.rear = 0
        self.size = k + 1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.array[self.rear] = value
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.size
            # 不需要重制为0
            # self.array[self.front] = 0
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.array[(self.front + 1) % self.size]
    
    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.array[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.front == (self.rear + 1) % self.size


'''Bad Version: nenecessary if/else checks'''
class MyCircularQueue:

    def __init__(self, k):
        self.size = 0
        self.max_size = k
        self.t = [0]*k
        self.front = self.rear = -1
        
    def enQueue(self, value):
        if self.size == self.max_size: return False
        else:
            if self.rear == -1:
                self.rear = self.front = 0
            else:
                self.rear = (self.rear + 1)%self.max_size
            self.t[self.rear] = value
            self.size += 1
            return True
        
    def deQueue(self):
        if self.size == 0: return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1)%self.max_size
        self.size -= 1
        return True
        

    def Front(self):
        return self.t[self.front] if self.size != 0 else -1

    def Rear(self):
        return self.t[self.rear] if self.size != 0 else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size