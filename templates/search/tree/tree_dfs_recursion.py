from typing import Optional, List
from templates.common_data_structures.tree_node import TreeNode


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
