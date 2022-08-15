class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


class Solution:
    def romanToInt(self, s):
        _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        sum = 0
        for i in s[::-1]:
            curr = _dict[i]
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
        return sum
