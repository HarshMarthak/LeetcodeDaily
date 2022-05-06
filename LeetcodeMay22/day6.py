#two similar solutions
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter = 0
        lastChr = ''
        s += ' '
        for i in s:
            if i == lastChr:
                counter += 1
            else:
                v = counter % k
                if v>0:
                    stack.append((lastChr, v))
                    counter = 1

                elif len(stack) > 0 and stack[-1][0] == i:
                    st, counter = stack.pop()
                    counter += 1
                else:

                    counter = 1
                lastChr = i

        s = ''
        for i in stack:
            s += i[0] * i[1]
        return s

#######################################################################################

class Solution:
    def removeDuplicates(self, s, k):
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

