class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}
        result = float("inf")
        def dfs(i):
            nonlocal result
            if i >= len(nums)-1:
                return 0

            if nums[i] == 0:
                return float("inf")

            if i in memo:
                return memo[i]
            
            for num in range(nums[i], 0, -1):
                result = min(result, 1 + dfs(i + num))
                memo[i] = result

            return memo[i]

        return dfs(0)