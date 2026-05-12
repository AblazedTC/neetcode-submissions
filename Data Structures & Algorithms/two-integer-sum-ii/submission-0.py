class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointer solution
        l, r = 0, 0
        n = len(numbers)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if numbers[i] + numbers[j] == target:
                    return [min(i+1, j+1), max(i+1, j+1)]
