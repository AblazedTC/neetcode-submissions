class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        cur = head

        # move end n steps ahead
        for _ in range(n):
            end = end.next

        # if end is None, remove head
        if not end:
            return head.next

        # move both pointers
        while end.next:
            end = end.next
            cur = cur.next

        # delete node
        cur.next = cur.next.next

        return head