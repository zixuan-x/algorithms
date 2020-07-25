# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur = root
        self.pushAll()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self.stack.pop()
        self.cur = res.right
        self.pushAll()
        return res.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack
        
    def pushAll(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()