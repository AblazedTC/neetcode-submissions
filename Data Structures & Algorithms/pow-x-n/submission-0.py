class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        ogX = x
        power = abs(n)

        for i in range(power - 1):
            x = x * ogX

        if n < 0:
            return 1 / x

        return x