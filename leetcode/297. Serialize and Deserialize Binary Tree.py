from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        nodes = [str(root.val)]
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                nodes.append(str(node.left.val))
            else:
                nodes.append('#')
            if node.right:
                queue.append(node.right)
                nodes.append(str(node.right.val))
            else:
                nodes.append('#')
        return ','.join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        index = 1
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if nodes[index] != '#':
                cur.left = TreeNode(int(nodes[index]))
                queue.append(cur.left)
            index += 1
            if nodes[index] != '#':
                cur.right = TreeNode(int(nodes[index]))
                queue.append(cur.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))