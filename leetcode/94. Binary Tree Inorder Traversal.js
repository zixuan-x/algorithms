/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

 // 1. recursive
var inorderTraversal = function(root) {
    if (root == null) {
        return [];
    }
    
    const left = inorderTraversal(root.left);
    const right = inorderTraversal(root.right);
    return [...left, root.val, ...right];
};

// 2. iterative
var inorderTraversal = function(root) {
    const stack = [];
    const result = [];
    let cur = root;
    while (cur != null || stack.length > 0) {
        if (cur != null) {
            stack.push(cur);
            cur = cur.left;
        } else {
            cur = stack.pop();
            result.push(cur.val);
            cur = cur.right;
        }
    }
    return result;
};