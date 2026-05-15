import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        heap = []
        sortedArray = []
        #both arrays can be empty
        
        if nums1:
            heapq.heappush(heap, (nums1[0], nums1, 0))
            
        if nums2:
            heapq.heappush(heap, (nums2[0], nums2, 0))
        
        while heap:
            num, listnum, index = heapq.heappop(heap)
            sortedArray.append(num)
            if index + 1 < len(listnum):
                heapq.heappush(heap, (listnum[index+1], listnum, index+1))
            
        print(sortedArray)
        totalLen = len(sortedArray)
        
        if totalLen % 2 != 0:
            return sortedArray[totalLen // 2]
        else:
            return (sortedArray[totalLen // 2] + sortedArray[(totalLen // 2) - 1]) / 2
            