# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            ls = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    ls.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if ls:
                ans.append(ls[len(ls)-1])

        return ans


        
        