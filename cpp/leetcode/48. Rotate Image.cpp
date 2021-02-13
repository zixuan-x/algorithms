#include <vector>
using std::vector;
#include <algorithm>
using std::swap;

// https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // reverse up to down
        reverse(matrix.begin(), matrix.end());
        // reverse diagonaly
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = i + 1; j < matrix[i].size(); j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};