class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            if tree1.val != tree2.val:
                return False
            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)

        def search(node, subRoot):
            if node is None:
                return False
            
            if isSameTree(node, subRoot):
                return True
            
            return search(node.left, subRoot) or search(node.right, subRoot)

        return search(root, subRoot)