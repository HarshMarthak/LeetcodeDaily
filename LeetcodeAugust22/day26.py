class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        l=sorted(list(str(n)))
        for i in range(30):
            a=2**i
            b=sorted(list(str(a)))
            if l==b:
                return True
        return False
