class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        curSet = []

        def search(i):
            if i == len(nums):
                print("curSet")
                ans.append(curSet.copy())
                return

            print("test")

            #Take
            curSet.append(nums[i])
            search(i + 1)
            curSet.pop()


            #Not Take
            currentNum = nums[i]
            while i < len(nums) and nums[i] == currentNum:
                i += 1
            search(i)
            
        search(0)
        return ans
        