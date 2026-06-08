class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        def simulate(startPos):
            curGas = 0
            curIndex = startPos

            for _ in range(n):
                curGas += gas[curIndex]

                if curGas < cost[curIndex]:
                    return -1

                curGas -= cost[curIndex]
                curIndex = (curIndex + 1) % n

            return startPos

        for index in range(n):
            ans = simulate(index)
            if ans != -1:
                return ans

        return -1