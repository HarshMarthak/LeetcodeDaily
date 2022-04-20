class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.push(root)
    def next(self) -> int:
        temp = self.stack.pop()
        self.push(temp.right)
        return temp.val
    def hasNext(self) -> bool:
        return self.stack
    def push(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
