class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d={}
        ans=[]
        if not root:
            return
        def recur(root,level):
            if root==None:
                return
            if level not in d:
                d[level]=[]
            d[level].append(root.val)
            recur(root.left,level+1)
            recur(root.right,level+1)
        recur(root,0)
        for a in d:
            ans.append(d[a])
        return ans

#removed dictionary because not necessary

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return

        def recur(root,level,ans):
            if root==None:
                return
            if level==len(ans):
                ans.append([])
            ans[level].append(root.val)
            recur(root.left,level+1,ans)
            recur(root.right,level+1,ans)

        recur(root,0,ans)
        return ans
