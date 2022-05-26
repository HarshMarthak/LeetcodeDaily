#two solutions

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        for i in range(32,-1,-1):
            if n==0:
                break
            temp = n%2**i
            if temp!=n:
                count+=1
            n=temp
        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')
