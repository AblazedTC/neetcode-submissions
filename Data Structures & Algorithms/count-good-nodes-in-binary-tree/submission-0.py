# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(node, maxVal):
            if not node:
                return 0

            good = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            return good + search(node.left, maxVal) + search(node.right, maxVal)

        if not root:
            return 0

        return search(root, root.val)