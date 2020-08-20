'''
heap:
addScore: O(1)
top: O(nlogk) -> can also be O(n + klogn)
reset: O(1)
'''
class Leaderboard:

    def __init__(self):
        self.player = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.player[playerId] += score

    def top(self, K: int) -> int:
        minHeap = []
        for score in self.player.values():
            heappush(minHeap, score)
            if len(minHeap) > K:
                heappop(minHeap)
        return sum(minHeap)

    def reset(self, playerId: int) -> None:
        self.player[playerId] = 0

'''
sort:
addScore: O(1)
top: O(nlogn)
reset: O(1)
'''
class Leaderboard:

    def __init__(self):
        self.player = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.player[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.player.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self.player[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)