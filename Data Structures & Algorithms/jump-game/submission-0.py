class Solution:
    def canJump(self, nums: List[int]) -> bool:

        #Memoization
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if i in memo:
                return memo[i]

            for jump in range(nums[i], 0, -1):
                if dfs(i + jump):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)

        