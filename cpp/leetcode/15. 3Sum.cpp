#include <vector>
using std::vector;
#include <algorithm>

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        
        std::sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); i++) {
            int target = -nums[i];
            int front = i + 1;
            int back = nums.size() - 1;
            
            while (front < back) {
                int sum = nums[front] + nums[back];
                // Finding answer which start from number num[i]   
                if (sum < target)
                    front++;
                else if (sum > target)
                    back--;
                else {
                    vector<int> triplet{nums[i], nums[front], nums[back]};
                    results.push_back(triplet);
                    
                    // Processing duplucates of Number 2
                    // Rolling the front pointer to the next different number forwards
                    while (front < back && nums[front] == triplet[1]) front++;
                    
                    // Processing duplicates of Number 3
                    // Rolling the back pointer to the next different number backwards
                    while (front < back && nums[back] == triplet[2]) back--;
                }
            }
            
            // Processing duplicates of Number 1
            while (i + 1 < nums.size() && nums[i + 1] == nums[i])
                i++;
        }
        return results;
    }
};