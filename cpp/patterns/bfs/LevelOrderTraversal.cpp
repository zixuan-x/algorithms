#include <iostream>
#include <queue>
#include "../util/TreeNode.h"

using namespace std;

/** 
 * n = total number of nodes in the tree
 * time: O(n)
 * space: O(n/2) = O(n)
 */ 
class LevelOrderTraversal {
public:
    static vector<vector<int>> traverse(TreeNode *root) {
        vector<vector<int>> result;
        if (root == nullptr) 
            return result;
        
        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            for (int i = 0; i < levelSize; i++) {
                TreeNode *node = q.front();
                q.pop();
                level.push_back(node->val);
                if (node->left!= nullptr) {
                    q.push(node->left);
                }
                if (node->right!= nullptr) {
                    q.push(node->right);
                }
            }
            result.push_back(level);
        }
        return result;
    }
};

int main(int argc, char *argv[]) {
    TreeNode *root = new TreeNode(12);
    root->left = new TreeNode(7);
    root->right = new TreeNode(1);
    root->left->left = new TreeNode(9);
    root->right->left = new TreeNode(10);
    root->right->right = new TreeNode(5);

    vector<vector<int>> result = LevelOrderTraversal::traverse(root);
    cout << "Level order traversal: ";
    for (auto vec : result) {
        for (auto num : vec) {
            cout << num << " ";
        }
        cout << endl;
    }
}