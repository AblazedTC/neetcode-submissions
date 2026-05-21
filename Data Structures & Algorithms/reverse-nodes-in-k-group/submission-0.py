class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check if we have k nodes
        cur = head
        for i in range(k):
            if not cur:
                return head
            cur = cur.next

        prev = None
        cur = head

        # reverse k nodes
        for i in range(k):
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        # head is now the end of this reversed group
        head.next = self.reverseKGroup(cur, k)

        return prev