class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.ans=[]
        def traverse(root,lvl):
            if not root:
                return
            if len(self.ans)<lvl+1:
                self.ans.append([])
            self.ans[lvl].append(root.val)
            for child in root.children:
                traverse(child,lvl+1)
        traverse(root,0)
        return self.ans
