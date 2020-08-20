'''
checkInUsers = {id: (start station, start time)}
averageTime = {(start, end): (averageTime, trips)}

space: O(total number of ids) + O(n ^ 2) where n = number of stations

checkIn: time: O(1) 
1. store checkedin users {id: (station, time)}

checkOut: time: O(1)
1. get the checkin user by id -> (station, time)
2. calculate average time by adding this trip
    averageTime = (averageTime * trips + (endtime - starttime)) // (trips + 1)
    trips += 1

getAverageTime: time: O(1)
1. get from dict
'''

class UndergroundSystem:

    def __init__(self):
        self.checkedInUsers = {}  # {id: (start station, start time)}
        self.averageTimes = {}  # {(start, end): (averageTime, trips)}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # 1. store checkedin users {id: (station, time)}
        self.checkedInUsers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # 1. get the checkin user by id -> (station, time)
        startStation, startTime = self.checkedInUsers[id]
        
        endStation, endTime = stationName, t
        # 2. calculate average time by adding this trip
        trip = (startStation, endStation) if startStation < endStation else (endStation, startStation)
        average, count = self.averageTimes.get(trip, (0, 0))
        self.averageTimes[trip] = ((average * count + (endTime - startTime)) / (count + 1), count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation, endStation) if startStation < endStation else (endStation, startStation)
        return self.averageTimes[trip][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)