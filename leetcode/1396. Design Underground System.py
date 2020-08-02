class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}  # {id: stationName, t}
        self.averages = {}  # {(stationName1, stationName2): averageTime, numberOfTrips}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns[id]
        endStation, endTime = stationName, t
        travel = (startStation, endStation) if startStation < endStation else (endStation, startStation)
        averageTime, numberOfTrips = self.averages.get(travel, (0, 0))
        self.averages[travel] = (averageTime * numberOfTrips + (endTime - startTime)) / (numberOfTrips + 1), (numberOfTrips + 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation) if startStation < endStation else (endStation, startStation)
        return self.averages[travel][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)