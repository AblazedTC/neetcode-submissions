class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None:
                return

            temp = node.left
            node.left = node.right
            node.right = temp

            invert(node.left)
            invert(node.right)
        
        invert(root)
        return root