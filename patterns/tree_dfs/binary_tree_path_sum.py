# Given a binary tree and a number ‘S’, find if the tree has a path from
# root-to-leaf such that the sum of all the node values of that path equals ‘S’.
from typing import Optional

from templates.common_data_structures.tree_node import TreeNode


def has_path(root: Optional[TreeNode], total: int) -> bool:
    """
    Recursion

    Time Complexity: O(n)
    Space Complexity: O(h), where h is the height of the tree. In the worst case, h == n.
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == total
    return has_path(root.left, total - root.val) or has_path(root.right, total - root.val)


def has_path_stack(root, total):
    if not root:
        return False

    running_sum = 0
    cur = root
    stack = []  # (node, visited?)
    while cur or stack:
        if cur:
            stack.append((cur, False))
            running_sum += cur.val
            cur = cur.left
        else:
            cur, visited = stack.pop()
            if visited:
                if not cur.left and not cur.right and running_sum == total:
                    return True
                else:
                    running_sum -= cur.val
                    cur = None
            else:
                stack.append((cur, True))
                cur = cur.right
    return False


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    assert has_path_stack(root, 23)
    assert not has_path_stack(root, 16)


main()
