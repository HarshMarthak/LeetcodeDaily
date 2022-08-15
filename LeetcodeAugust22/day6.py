class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        return ceil(log(buckets) / log(states))