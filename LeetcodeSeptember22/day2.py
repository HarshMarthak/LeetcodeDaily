#bfs
class Solution:
    def averageOfLevels(self, root):
        queue = deque([root])
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(sum(level)/len(level))
        return result
#dfs
import math
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.ans=[]
        def dfs(root,lvl):
            # print(self.ans)
            if not root:
                return
            if len(self.ans)<lvl+1:
                self.ans.append([])
            self.ans[lvl].append(root.val)
            dfs(root.left,lvl+1)
            dfs(root.right,lvl+1)
        dfs(root,0)
        self.ans[0]=self.ans[0][0]
        for i in range(1,len(self.ans)):
            self.ans[i]=round((sum(self.ans[i])/len(self.ans[i])),5)
        return self.ans
