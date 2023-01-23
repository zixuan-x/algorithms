from typing import Optional, List
from templates.common_data_structures.tree_node import TreeNode


# 1. Push only left nodes onto Stack
def pre_order(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return result

    cur = root
    stack = []
    while cur or stack:
        if cur:
            result.append(cur.val)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            cur = cur.right
    return result


def in_order(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return result

    cur = root
    stack = []
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    return result


def post_order_mirror(root: Optional[TreeNode]) -> List[int]:
    # mirror the tree and do a pre-order traversal
    result = []  # can also use a deque and appendleft
    if not root:
        return result

    cur = root
    stack = []
    while cur or stack:
        if cur:
            stack.append(cur)
            result.append(cur.val)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left
    return result[::-1]


def post_order_push_twice(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return result

    cur = root
    stack = []
    while cur or stack:
        if cur:
            stack.append((cur, False))  # (node, visited?)
            cur = cur.left
        else:
            cur, visited = stack.pop()
            if visited:
                result.append(cur.val)
                cur = None
            else:
                stack.append((cur, True))
                cur = cur.right
    return list(result)


# 2. Push all nodes onto Stack
def pre_order_push_all(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return result

    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            result.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
    return result


def in_order_push_all(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return result

    stack = [(root, False)]  # (node, visited)
    while stack:
        cur, visited = stack.pop()
        if cur:
            if visited:
                result.append(cur.val)
            else:
                stack.append((cur.right, False))
                stack.append((cur, True))
                stack.append((cur.left, False))
    return result


def post_order_push_all(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return result

    stack = [(root, False)]  # (node, visited?)
    while stack:
        cur, visited = stack.pop()
        if cur:
            if visited:
                result.append(cur.val)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
    return result
