# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        heap = []
        tiebreak = 0

        #adding every node to heap
        for node in lists:
            while node:
                heapq.heappush(heap, (node.val, tiebreak, node))
                node = node.next
                tiebreak += 1

        #adding minValue node to new list
        while heap:
            _, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

        return head.next

        