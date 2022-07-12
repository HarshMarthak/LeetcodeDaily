class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n, sides = len(matchsticks), sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        if sides != sum(matchsticks)/4 or matchsticks[0] > sides:
            return False
        def backtracking(i, total, chk):
            if chk == 3:
                return True
            while i < n:
                num = matchsticks[i]
                if num > total:
                    i += 1
                    continue
                matchsticks[i] = sides + 1
                if num == total:
                    res = backtracking(1, sides, chk+1)
                else:
                    res = backtracking(i+1, total-num, chk)
                if res:
                    return True
                matchsticks[i] = num
                while i < n and matchsticks[i] == num:
                    i += 1
            return False
        return backtracking(0, sides, 0)
