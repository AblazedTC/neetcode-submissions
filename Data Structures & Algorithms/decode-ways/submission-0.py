class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        def dfs(i):
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            # Take 1 digit
            total = dfs(i + 1)

            # Take 2 digits if valid
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                total += dfs(i + 2)
                
            memo[i] = total
            return memo[i]

        return dfs(0)