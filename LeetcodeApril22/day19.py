class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        pre = first = second = None
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if not first and pre and pre.val > node.val:
                first = pre
            if first and pre and pre.val > node.val:
                second = node
            pre = node
            root = node.right
        first.val, second.val = second.val, first.val
