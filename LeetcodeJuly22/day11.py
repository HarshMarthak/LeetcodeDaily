from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        res = []
        while queue:
            level = len(queue)
            nodes = []
            for _ in range(level):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(nodes.pop())
        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def solve(root, lvl):
            if root:
                if len(res)==lvl:
                    res.append(root.val)
                solve(root.right, lvl + 1)
                solve(root.left, lvl + 1)
            return
        res = []
        solve(root,0)
        return res
