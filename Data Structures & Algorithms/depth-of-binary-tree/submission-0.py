# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def search(node, length):
            nonlocal globalLen

            if node is None:
                globalLen = max(globalLen, length)
                return
            
            search(node.left, length + 1)
            search(node.right, length + 1)

        globalLen = 0
        search(root, 0)
        return globalLen
        