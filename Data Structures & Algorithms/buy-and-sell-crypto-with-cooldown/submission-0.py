class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        def search(i, haveCoin):
            if i >= len(prices):
                return 0

            if (i, haveCoin) in memo:
                return memo[(i, haveCoin)]

            # Carrying Coin
            if haveCoin == True:
                memo[(i, haveCoin)] = max(
                    # Sold Coin
                    prices[i] + search(i + 2, False),
                    # Heald onto coin
                    search(i + 1, True),
                )

            # No Coin
            else:
                memo[(i, haveCoin)] = max(
                    # Bought Coin
                    search(i + 1, True) - prices[i],
                    # Did nothing
                    search(i + 1, False),
                )

            return memo[(i, haveCoin)]

        return search(0, False)