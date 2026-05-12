# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #we can determine if a Linked list has a cycle by using 2 points (fast and slow)
        #at any point if fast = slow then there is a detected cycle
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
            
        return False
        