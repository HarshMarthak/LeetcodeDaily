class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return
        ans=[]
        def helper(root,path):
            if root:
                path.append(root.val)
                if (not root.left and not root.right) and sum(path)==targetSum:
                    ans.append(path.copy())
                helper(root.left,path)
                helper(root.right,path)
                path.pop()
        helper(root,[])
        return ans
