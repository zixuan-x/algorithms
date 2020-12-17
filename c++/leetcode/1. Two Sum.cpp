#include <vector>
using std::vector;
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash; // {value: index}
        vector<int> result = {-1, -1};
        for (int i = 0; i < nums.size(); i++) {
            int numberToFind = target - nums.at(i);
            if (hash.find(numberToFind) != hash.end()) {
                result = {hash[numberToFind], i};
                return result;
            }
            hash[nums.at(i)] = i;
        }
        return result;
    }
};