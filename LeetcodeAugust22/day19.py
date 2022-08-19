class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ncount = dict()
        for num in nums:
            if num not in ncount:
                ncount[num] = 0
            ncount[num] += 1

        sequences = []
        for num in sorted(ncount.keys()):
            count = ncount[num]
            s = len(sequences)-1
            for _ in range(count):
                if s>= 0 and sequences[s][-1] + 1 == num:
                    sequences[s].append(num)
                    s -= 1
                else:
                    sequences.append([num])

        for sequence in sequences:
            if len(sequence) < 3:
                return False

        return True

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True
