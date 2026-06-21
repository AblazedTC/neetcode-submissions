class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for j in range(len(text2) - 1, -1, -1):      # rows: text2
            for i in range(len(text1) - 1, -1, -1):  # cols: text1

                if text2[j] == text1[i]:
                    dp[j][i] = 1 + dp[j + 1][i + 1]
                else:
                    dp[j][i] = max(dp[j + 1][i], dp[j][i + 1])

        return dp[0][0]