class Solution:
    def increasingBST(self, root: TreeNode,Tail=None) -> TreeNode:
        if not root:
            return Tail
        ans=self.increasingBST(root.left,root)
        root.left=None
        root.right=self.increasingBST(root.right,Tail)
        return ans
