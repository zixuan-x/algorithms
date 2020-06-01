from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        self.preOrder(root, res)
        return ' '.join(map(str, res))
        
    def preOrder(self, root, res):
        if not root: return
        res.append(root.val)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        values = deque(map(int, data.split()))
        return self.build(values, float('-inf'), float('inf'))
        
    def build(self, values, minValue, maxValue):
        if values and minValue < values[0] < maxValue:
            value = values.popleft()
            root = TreeNode(value)
            root.left = self.build(values, minValue, value)
            root.right = self.build(values, value, maxValue)
            return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))