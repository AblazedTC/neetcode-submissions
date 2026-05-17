class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curCombo = []

        def backtrack(openCount, closeCount):
            if openCount == n and closeCount == n:
                ans.append("".join(curCombo))
                return

            if openCount < n:
                curCombo.append("(")
                backtrack(openCount + 1, closeCount)
                curCombo.pop()

            if closeCount < openCount:
                curCombo.append(")")
                backtrack(openCount, closeCount + 1)
                curCombo.pop()

        backtrack(0, 0)
        return ans