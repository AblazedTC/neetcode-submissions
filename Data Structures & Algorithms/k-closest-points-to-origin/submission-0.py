import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        print(points)
        # Calculate and put distance and coordinates in min heap and pop top k
        heap = []

        for x, y in points:
            distance = math.sqrt(((x - 0)**2) + ((y - 0)**2))
            heapq.heappush(heap, (distance, x, y))
        
        ans = []
        for i in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans





        