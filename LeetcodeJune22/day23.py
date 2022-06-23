#my solution

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        temp = []
        start = 0
        for t, end in sorted(courses, key = lambda x:x[1]):
            start += t
            heapq.heappush(temp, -t)
            while start > end:
                start += heapq.heappop(temp)
        return len(temp)


#alternate solution

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        t = 0
        courses.sort(key=lambda x: x[1])
        heap = []
        for dur, due in courses:
            if t + dur <= due:
                t += dur
                heapq.heappush(heap, -dur)
            elif heap and -heap[0] > dur:
                t += heapq.heappop(heap)
                t += dur
                heapq.heappush(heap, -dur)
        return len(heap)
