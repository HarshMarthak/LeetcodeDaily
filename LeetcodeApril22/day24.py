class UndergroundSystem:
    def __init__(self):
        self.Map = {}
        self.time = defaultdict(int)
        self.count = defaultdict(int)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.Map[id] = [stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn = self.Map.pop(id)
        self.time[(checkIn[0], stationName)] += t - checkIn[1]
        self.count[(checkIn[0], stationName)] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routeName = (startStation, endStation)
        return self.time[routeName] / self.count[routeName]
