from collections import defaultdict, deque
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.followeeIds = defaultdict(set)
        self.posts = defaultdict(deque)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        user_tweets = self.posts[userId]

        for i in range(min(10, len(user_tweets))):
            heapq.heappush(heap, user_tweets[i])

        for followee in self.followeeIds[userId]:
            tweets = self.posts[followee]

            for i in range(min(10, len(tweets))):
                if len(heap) < 10:
                    heapq.heappush(heap, tweets[i])
                elif len(heap) == 10 and heap[0] < tweets[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, tweets[i])

        if not heap:
            return []

        return [heapq.heappop(heap)[1] for _ in range(len(heap))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followeeIds[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeIds[followerId]:
            self.followeeIds[followerId].remove(followeeId)
            
