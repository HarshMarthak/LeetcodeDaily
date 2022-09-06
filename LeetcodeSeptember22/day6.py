class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val: return None
        return root


class Solution:
    def dfs(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return False
        ret = False
        if self.dfs(node.left):
            ret = True
        else:
            node.left = None

        if self.dfs(node.right):
            ret = True
        else:
            node.right = None

        return ret or (node.val == 1)

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return root if self.dfs(root) else None
