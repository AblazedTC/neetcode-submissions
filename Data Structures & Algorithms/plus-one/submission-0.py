class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number *= 10
            number += digit
        number += 1

        ans = []
        while number != 0:
            print(number%10)
            ans.insert(0,number%10)
            number = number // 10

        return ans