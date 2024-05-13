from collections import defaultdict
import heapq

class Tweet:
    def __init__(self, tweetId, timestamp):
        self.id = tweetId
        self.timestamp = timestamp
        self.next = None

    def __lt__(self, other):
        return self.timestamp > other.timestamp


class Twitter:

    def __init__(self):
        self.followings = defaultdict(set)
        self.tweets = defaultdict(lambda: None)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        tweet = Tweet(tweetId, self.timestamp)
        tweet.next = self.tweets[userId]
        self.tweets[userId] = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        heap = []

        tweet = self.tweets[userId]
        if tweet:
            heap.append(tweet)

        for user in self.followings[userId]:
            tweet = self.tweets[user]
            if tweet:
                heap.append(tweet)
        heapq.heapify(heap)

        while heap and len(tweets) < 10: # pop 10 latest head node
            head = heapq.heappop(heap)
            tweets.append(head.id)

            if head.next:
                heapq.heappush(heap, head.next) # keep the heap relations
            
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followings[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)