from collections import deque
from typing import Optional, List

from templates.common_data_structures.graph_node import Node


def breadth_first_search(self, node: Optional[Node]) -> List[int]:
    if not node:
        return []

    result = []

    queue = deque([node])
    visited = {node}  # same as: set([node])
    while queue:
        cur = queue.popleft()
        result.append(cur.val)
        for child in cur.neighbors:
            if child not in visited:
                visited.add(child)
                queue.append(child)
    return result
