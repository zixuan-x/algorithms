#include <vector>
using std::vector;
#include <queue>
using std::queue;
#include <utility>
using std::pair;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size(), count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    search(grid, i, j);
                }
            }
        }
        return count;
    }

private:
    // depth-first search
    void search(vector<vector<char>>& grid, int i, int j) {
        int m = grid.size(), n = grid[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0') 
            return;
        grid[i][j] = '0';
        search(grid, i + 1, j);
        search(grid, i - 1, j);
        search(grid, i, j + 1);
        search(grid, i, j - 1);
    }

    // breadth-first search
    void search2(vector<vector<char>>& grid, int i, int j) {
        int m = grid.size(), n = grid[0].size();
        grid[i][j] = '0';
        queue<pair<int, int>> nodes;
        nodes.push({i, j});
        while(!nodes.empty()) {
            pair<int, int> node = nodes.front();
            nodes.pop();
            int x = node.first, y = node.second;
            int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            for (int k = 0; k < 4; k++) {
                int dx = x + directions[k][0];
                int dy = y + directions[k][1];
                if (dx >= 0 && dx < m && dy >= 0 && dy < n && grid[dx][dy] == '1') {
                    nodes.push({dx, dy});
                    grid[dx][dy] = '0';
                }
            }
        }
    }
};