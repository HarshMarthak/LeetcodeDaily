class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(numbers):
            needed = target - num
            if needed in mydict.keys():
                return [mydict[needed]+1, i+1]
            else:
                mydict[num] = i
