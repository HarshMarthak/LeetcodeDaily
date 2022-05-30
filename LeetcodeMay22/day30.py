#my solution
class Solution:
    def divide(self, a, b):
        if (a == -2147483648 and b == -1): return 2147483647
        neg=1
        if a<0 or b<0:
            neg=-1
        if a<0 and b<0:
            neg=1
        a,b=abs(a),abs(b)
        count=0
        temp=0
        for i in range(31, -1, -1):
            if (temp + (b << i) <= a):
                temp += b << i;
                count |= 1 << i;
        if neg ==-1 :
            count=-count;
        return count;
#better solution
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2 ** 31
        INT_MIN_HALF = INT_MIN // 2
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = 2
        if dividend > 0:
            negative -= 1
            dividend = -dividend
        if divisor > 0:
            negative -= 1
            divisor = -divisor
        doubles = []
        i = 1
        while dividend <= divisor:
            doubles.append((divisor, i))
            if divisor < INT_MIN_HALF:
                break
            divisor += divisor
            i += i

        res = 0
        for i in range(len(doubles)-1, -1, -1):
            if dividend <= doubles[i][0]:
                dividend -= doubles[i][0]
                res += doubles[i][1]

        return -res if negative == 1 else res
