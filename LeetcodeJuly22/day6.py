# my solution

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        p1 = 0
        p2 = 1
        for i in range(2, n+1):
            p2, p1 = p1+p2, p2
        return p2

# troll solution

class Solution:
    def fib(self, n: int) -> int:
        ans=[0,1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        return ans[n]
