from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        q = deque()
        q.append((amount, 0))

        seen = set()
        seen.add(amount)

        while q:
            amountRemaining, numCoins = q.popleft()

            if amountRemaining == 0:
                return numCoins

            for coin in coins:
                newAmount = amountRemaining - coin

                if newAmount >= 0 and newAmount not in seen:
                    seen.add(newAmount)
                    q.append((newAmount, numCoins + 1))

        return -1