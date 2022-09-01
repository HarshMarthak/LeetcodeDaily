class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def dfs(root,currMax):
            if not root:
                return
            if root.val>=currMax:
                self.count+=1
                currMax=max(currMax,root.val)
            dfs(root.left,currMax)
            dfs(root.right,currMax)
        dfs(root,-10001)
        return self.count
