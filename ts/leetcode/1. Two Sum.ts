// brute force: O(n ^ 2)
function twoSum1(nums: number[], target: number): number[] {
    if (!nums) {
        return [-1, -1];
    }

    for (let i = 0; i < nums.length; i ++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }

    return [-1, -1];
};

// hash table:
function twoSum(nums: number[], target: number): number[] {
    const hashtable: {[index: number]: number} = {};
    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i];
        if (hashtable[diff] !== undefined) return [hashtable[diff], i];
        hashtable[nums[i]] = i;
    }
    return [-1, -1];
}