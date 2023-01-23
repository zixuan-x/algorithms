from typing import Optional, List
from templates.search.tree.tree_node import TreeNode


# Recursion
def pre_order(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)


def in_order(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)


def post_order(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return post_order(root.left) + post_order(root.right) + [root.val]


# Stack
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


# mirror the tree and do a pre-order traversal
def post_order_mirror(root: Optional[TreeNode]) -> List[int]:
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


def post_order_push_all_twice(root: Optional[TreeNode]) -> List[int]:
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
