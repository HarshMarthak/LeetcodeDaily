class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left_limit, right_limit):
            if not node:
                return True
            
            if left_limit < node.val < right_limit:
                return dfs(node.left, left_limit, node.val) and dfs(node.right, node.val, right_limit)
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        myArr = []
        self.__inorderTraversal(root, myArr)
        
        N = len(myArr)
        for i in range(1,N):
            if myArr[i] <= myArr[i-1]:
                return False
        return True
    
    def __inorderTraversal(self, root, myArr):
        
        if root is None:
            return
        
        self.__inorderTraversal(root.left, myArr)
        myArr.append(root.val)
        self.__inorderTraversal(root.right, myArr)
        
        return