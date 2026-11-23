#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;

        for (size_t i = 0; i < nums.size(); i++) {
            if (seen.contains(nums[i])) {
                return true;
            }
            seen.insert(nums[i]);
        }

        return false;
    }
};