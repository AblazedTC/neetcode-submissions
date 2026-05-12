class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = (l + r) // 2

            if nums[r] > nums[m]:
                r = m
                continue

            else:
                l = m + 1
                continue

        return nums[r]
            


        