#include <vector>
using std::vector;
#include <stack>
using std::stack;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// 1. recursive
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        preorderTraversal(root, result);
        return result;
    }
private:
    void preorderTraversal(TreeNode* root, vector<int>& result) {
        if (!root) return;
        result.push_back(root->val);
        preorderTraversal(root->left, result);
        preorderTraversal(root->right, result);
    }
};

// 2. iterative
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> result;
        stack<TreeNode*> s;
        TreeNode *cur = root;
        while (cur != nullptr || !s.empty()) {
            if (cur != nullptr) {
                result.push_back(cur->val);
                s.push(cur);
                cur = cur->left;
            } else {
                cur = s.top(); s.pop();
                cur = cur->right;
            }
        }
        return result;
    }
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right) {}
};
