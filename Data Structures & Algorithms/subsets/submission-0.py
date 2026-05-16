class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        currentSubset = []


        def search(i):
            if i == len(nums):
                result.append(currentSubset.copy())
                return

            #Take num
            currentSubset.append(nums[i])
            search(i + 1)

            #Not Take num
            currentSubset.pop()
            search(i + 1)

        search(0)
        return result