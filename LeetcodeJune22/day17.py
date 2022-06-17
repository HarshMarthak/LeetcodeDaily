class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal result
            if node == None: return 2
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.left == 2 and node.right == 2:return 0
            if node.left == 0 or node.right == 0:
                result += 1
                return 1
            if node.left == 1 or node.right == 1:
                return 2
        result = 0

        if dfs(root) == 0:
            result += 1
        return result
