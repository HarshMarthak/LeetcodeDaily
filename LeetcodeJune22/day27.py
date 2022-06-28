class Solution:
    def minPartitions(self, n: str) -> int:
        temp=''
        for i in n:
            if i>temp:
                temp=i
        return int(temp)
