class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def change(node, val=0):
            if node:
                node.val += change(node.right, val)
                return change(node.left, node.val)
            else:
                return val
        change(root)
        return root
