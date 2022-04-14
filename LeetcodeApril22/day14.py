# iteration
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val==val:
                return root
            if root.val>val:
                root=root.left
            else:
                root=root.right
        return None
#recursion
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val==val:
            return root
        elif root.val>val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
