class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        subset = []

        def dfs(i, curSum):
            if curSum == target:
                ans.append(subset.copy())
                return

            if curSum > target or i >= len(candidates):
                return

            # Take num
            subset.append(candidates[i])
            dfs(i + 1, curSum + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Don't take num
            subset.pop()
            dfs(i + 1, curSum)

        dfs(0, 0)
        return ans
                