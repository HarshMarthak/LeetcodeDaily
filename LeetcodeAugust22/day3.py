import bisect
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        pos = bisect.bisect_left(self.booked, (start, end))

        if (pos == 0 or start >= self.booked[pos - 1][1]) and \
            (pos >= len(self.booked) or end <= self.booked[pos][0]):
            self.booked.insert(pos, (start, end))
            return True
        
        return False