class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}

        def dfs(i, amount):
            # Base Cases

            if amount == 0:
                return 1

            if amount < 0 or i == len(coins):
                return 0

            if (i, amount) in memo:
                return memo[(i, amount)]

            memo[(i, amount)] = dfs(i, amount - coins[i]) + dfs(i + 1, amount)

            return memo[(i, amount)]

        return dfs(0, amount)
