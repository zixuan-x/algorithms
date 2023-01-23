from collections import deque
from typing import Optional, List

from templates.common_data_structures.tree_node import TreeNode


def breadth_first_search(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        cur = queue.popleft()
        result.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return result


def breadth_first_search_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            cur = queue.popleft()
            level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        result.append(level)
    return result
