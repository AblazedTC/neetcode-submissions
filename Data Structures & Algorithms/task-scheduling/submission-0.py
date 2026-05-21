class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        freq = Counter(tasks)
        heap = []
        numsLeft = len(tasks)
        for key, val in freq.items():
            heapq.heappush_max(heap, (val, key))

        while numsLeft != 0:
            recentPop = []
            for _ in range(n + 1):
                if numsLeft == 0:
                    break
                if heap:
                    val, key = heapq.heappop_max(heap)
                    recentPop.append((val - 1, key))
                    ans += 1
                    numsLeft -= 1
                else:
                    ans += 1

            for val, key in recentPop:
                if val > 0:
                    heapq.heappush_max(heap, (val, key))
        return ans
