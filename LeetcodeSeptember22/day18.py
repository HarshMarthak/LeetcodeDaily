class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = height[0]
        rmax = height[-1]
        l = 1
        r = len(height)-2
        vol = 0
        while l <= r:
            if lmax >= rmax:
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    vol += rmax-height[r]
                r-=1
            else:
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    vol += lmax-height[l]
                l+=1
        return vol
