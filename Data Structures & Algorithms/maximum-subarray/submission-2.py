class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        ans = float("-inf")

        for num in nums:
            curSum = max(num, curSum + num)
            ans = max(ans, curSum)

        return ans