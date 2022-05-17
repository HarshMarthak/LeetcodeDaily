class Solution:
    res=TreeNode(None)

    def ans(self, original: TreeNode, cloned: TreeNode, target: TreeNode):
        if not original:
            return
        if original==target:
            self.res=cloned
        self.ans(original.left,cloned.left,target)
        self.ans(original.right,cloned.right,target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans(original,cloned,target)
        return self.res
