class Solution:
    def countOrders(self, n: int) -> int:
        mod=1000000007
        if n==0:
            return 1
        ans=n*(2*n-1)%mod
        ans=ans * Solution.countOrders(self,n-1) % mod
        return ans