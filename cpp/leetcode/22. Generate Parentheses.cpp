#include "vector"
using std::vector;
#include "string"
using std::string;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> results;
        generate(n, n, "", results);
        return results;
    }
private:
    void generate(int left, int right, string str, vector<string>& results) {
        // base cases
        if (left == 0 && right == 0) {
            results.push_back(str);
            return;
        }    
        
        // recursive rules
        if (left > 0) {
            generate(left - 1, right, str + "(", results);
        }
        if (left < right) {
            generate(left, right - 1, str + ")", results);
        }
    }
};
