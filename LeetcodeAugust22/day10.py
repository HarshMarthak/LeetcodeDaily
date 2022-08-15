class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    	return self.helper(nums, 0, len(nums))
    
    def helper(self, nums, lower, upper):
    	if lower == upper:
    		return None
    
    	mid = (lower + upper) // 2
    	node = TreeNode(nums[mid])
    	node.left = self.helper(nums, lower, mid)
    	node.right = self.helper(nums, mid+1, upper)
    
    	return node