class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSequence = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while length + num in nums:
                    length += 1
                maxSequence=max(maxSequence, length)
        return maxSequence
