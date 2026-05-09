import heapq
from collections import defaultdict


class AuctionSystem:

    def __init__(self):
        self.items = defaultdict(lambda: defaultdict(int))
        self.best_bids = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.items[itemId][userId] = bidAmount
        heapq.heappush(self.best_bids[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.items[itemId][userId] = newAmount
        heapq.heappush(self.best_bids[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.items[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        result = -1

        while self.best_bids[itemId]:
            amount, userId = self.best_bids[itemId][0]
            if self.items[itemId][-userId] == -amount:
                result = -userId
                break

            heapq.heappop(self.best_bids[itemId])

        return result