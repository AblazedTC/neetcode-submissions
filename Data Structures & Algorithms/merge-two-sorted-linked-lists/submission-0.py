import heapq

class Solution:
    def mergeTwoLists(self, list1, list2):
        heap = []
        i = 0

        if list1:
            heapq.heappush(heap, (list1.val, i, list1))
            i += 1
        if list2:
            heapq.heappush(heap, (list2.val, i, list2))
            i += 1

        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                i += 1

        return dummy.next