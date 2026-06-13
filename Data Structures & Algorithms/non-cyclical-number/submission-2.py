class Solution:
    def isHappy(self, n: int) -> bool:

        def calculate(inputNum):
            outputNum = 0

            while inputNum != 0:
                outputNum += (inputNum % 10) ** 2
                inputNum = inputNum // 10

            return outputNum

        seen = set()
        num = n

        while num not in seen:
            if num == 1:
                return True

            seen.add(num)
            num = calculate(num)

        return False