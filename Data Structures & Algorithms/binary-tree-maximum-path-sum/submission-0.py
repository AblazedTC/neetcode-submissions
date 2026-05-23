# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            leftTree = max(0, dfs(node.left))
            rightTree = max(0, dfs(node.right))

            ans = max(ans, node.val + leftTree + rightTree)

            return node.val + max(leftTree, rightTree)

        dfs(root)
        return ans