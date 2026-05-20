"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        if not head:
            return None

        # I think we can do 2 passes, for for node.next and another for node.random
        oldToNew = {}
        cur = Node(0)
        ans = cur

        oldHead = head

        # Val pass
        while head:
            oldToNew[head] = cur
            cur.val = head.val

            if head.next:
                cur.next = Node(-1)

            cur = cur.next
            head = head.next

        for key, value in oldToNew.items():
            value.random = oldToNew.get(key.random)

        return ans