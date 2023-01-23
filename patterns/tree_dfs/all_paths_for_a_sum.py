# Given a binary tree and a number ‘S’, find all paths from root-to-leaf
# such that the sum of all the node values of each path equals ‘S’.
from typing import Optional, List

from templates.common_data_structures.tree_node import TreeNode


def find_paths(root: Optional[TreeNode], total: int) -> List[List[int]]:
    """
    Recursion

    Time Complexity: O(n^2), where n is the total number of nodes.
        This is due to the fact that we traverse each node once (which will take
        O(n)), and for every leaf node, we might have to store its path (by making a
        copy of the current path) which will take O(n).

        We can calculate a tighter time complexity of O(NlogN) from
        the space complexity discussion below.

    Space Complexity: O()

    """
    paths = []
    path = []

    dfs(root, total, path, paths)

    return paths


def dfs(cur: Optional[TreeNode], total: int, path: List[int], paths: List[List[int]]) -> None:
    if not cur:
        return

    path.append(cur.val)

    if not cur.left and not cur.right:
        if cur.val == total:
            paths.append(path[:])
        path.pop()
        return

    dfs(cur.left, total - cur.val, path, paths)
    dfs(cur.right, total - cur.val, path, paths)

    path.pop()  # del path[-1]
