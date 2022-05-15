class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        prev, curr = [], [root]
        while curr:
            temp = []
            for n in curr:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            prev, curr = curr, temp
        return sum(x.val for x in prev)
