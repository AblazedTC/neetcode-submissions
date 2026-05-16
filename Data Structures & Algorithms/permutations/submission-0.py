class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        permutation = []
        taken = [False for _ in range(len(nums))]

        def dfs():
            if len(permutation) == len(nums):
                ans.append(permutation.copy())
                return

            for idx, num in enumerate(nums):
                if not taken[idx]:
                    permutation.append(num)
                    taken[idx] = True

                    dfs()

                    permutation.pop()
                    taken[idx] = False

        dfs()
        return ans