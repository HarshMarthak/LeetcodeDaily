class Solution:
    def minPartitions(self, n: str) -> int:
        temp=''
        for i in n:
            if i>temp:
                temp=i
        return int(temp)

#better solution LOL

class Solution:
    def minPartitions(self, n: str) -> int:
        if "9" in n:return 9
        if "8" in n:return 8
        if "7" in n:return 7
        if "6" in n:return 6
        if "5" in n:return 5
        if "4" in n:return 4
        if "3" in n:return 3
        if "2" in n:return 2
        if "1" in n:return 1
