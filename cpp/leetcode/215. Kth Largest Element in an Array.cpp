#include <vector>
using std::vector;
#include <queue>
using std::priority_queue;
#include <algorithm>
using std::greater;

class Solution {
public:
    /**
     * min-heap using priority_queue
     * time: O(nlogk)
     * space: O(k)
     */
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int num : nums) {
            pq.push(num);
            if (pq.size() > k) {
                pq.pop();
            }
        }
        return pq.top();
    }

    /** 
     * max-heap using priority_queue
     * time: O(n + klog(n))
     * space: O(n)
     */
    int findKthLargest1(vector<int>& nums, int k) {
        priority_queue<int> pq(nums.begin(), nums.end());
        for (int i = 0; i < k - 1; i++) {
            pq.pop();
        }
        return pq.top();
    }

    /**
     * max-heap using priority_queue
     * time: O(nlog(n - k + 1))
     * space: O(n)
     */
};