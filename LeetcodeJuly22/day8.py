#couldn't solve :( will try again later

#this isnt my solution í±¹â€¿í±¹

from functools import lru_cache
from heapq import heapify
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def get_answer(start, current_target):
            if start > m - current_target:
                return ((0, float('inf')), (1, float('inf')))
            if current_target == 0:
                if start < m:
                    return ((0, float('inf')), (1, float('inf')))
                else:
                    return ((0, 0), (1, 0))
            colorwise_mins = [float('inf')] * n
            colorwise_prefs = [0] * n
            restriction = None
            for end in range(start, m):
                if houses[end] != 0:
                    if restriction is None:
                        restriction = houses[end] - 1
                    elif restriction != houses[end] - 1:
                        break
                next_result = get_answer(end + 1, current_target - 1)
                if restriction is None:
                    for i in range(n):
                        colorwise_prefs[i] += cost[end][i]
                        new_value = colorwise_prefs[i] + (next_result[0][1] if i != next_result[0][0] else next_result[1][1])
                        colorwise_mins[i] = min(colorwise_mins[i], new_value)
                else:
                    if houses[end] == 0:
                        colorwise_prefs[restriction] += cost[end][restriction]
                    new_value = colorwise_prefs[restriction] + (next_result[0][1] if restriction != next_result[0][0] else next_result[1][1])
                    colorwise_mins[restriction] = min(colorwise_mins[restriction], new_value)
            heap = [(val, i) for i, val in enumerate(colorwise_mins)]
            heapify(heap)
            result = [(heap[0][1], heap[0][0])]
            if n == 1:
                result.append((1, float('inf')))
            elif n == 2 or heap[1] < heap[2]:
                result.append((heap[1][1], heap[1][0]))
            else:
                result.append((heap[2][1], heap[2][0]))
            return result
        answer = get_answer(0, target)[0][1]
        if answer < float('inf'):
            return answer
        else:
            return -1
