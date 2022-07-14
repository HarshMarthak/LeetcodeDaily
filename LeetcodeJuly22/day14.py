#my solution

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX+1:])

            return root

#better solution

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            nonlocal preorder_idx
            if left > right:
                return None

            val = preorder[preorder_idx]
            root = TreeNode(val)

            preorder_idx += 1

            root.left = helper(left, idx_map[val] - 1)
            root.right = helper(idx_map[val] + 1, right)

            return root

        preorder_idx = 0
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
