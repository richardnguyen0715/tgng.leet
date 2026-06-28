from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.clock = 0
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock += 1  # Increment clock first
        self.posts[userId].append((self.clock, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followers[userId]
        followeePosts = []
        
        # Get posts from all followees
        for followee in followees:
            posts = self.posts[followee]
            followeePosts.extend(posts)
        
        # Combine user's own posts with followee posts
        finalFeeds = self.posts[userId][:]  # Create a copy to avoid modifying original
        finalFeeds.extend(followeePosts)
        
        # Sort by timestamp (descending) and take top 10
        finalFeeds.sort(reverse=True)
        
        # Return only tweet IDs (not timestamps) and limit to 10
        return [tweetId for timestamp, tweetId in finalFeeds[:10]]

    def getNewsFeed2(self, userId: int) -> List[int]:
        followees = self.followers[userId]
        all_posts = []
        
        # Add user's own posts
        all_posts.extend(self.posts[userId])
        
        # Add followees' posts
        for followee in followees:
            all_posts.extend(self.posts[followee])
        
        # Use heap to get top 10 most recent tweets
        top_10 = heapq.nlargest(10, all_posts, key=lambda x: x[0])
        
        return [tweetId for timestamp, tweetId in top_10]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Don't allow following yourself
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Use discard instead of remove to avoid KeyError
        self.followers[followerId].discard(followeeId)
        
        

from collections import defaultdict
from typing import List

class TweetNode:
    def __init__(self, tweetId: int, timestamp: int):
        self.tweetId = tweetId
        self.timestamp = timestamp
        self.next = None

class Twitter:
    def __init__(self):
        self.clock = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(lambda: None)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock += 1
        new_tweet = TweetNode(tweetId, self.clock)
        new_tweet.next = self.tweets[userId]
        self.tweets[userId] = new_tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        # Collect all relevant linked list heads
        tweet_lists = []
        
        # Add user's own tweets
        if self.tweets[userId]:
            tweet_lists.append(self.tweets[userId])
        
        # Add followees' tweets
        for followeeId in self.followers[userId]:
            if self.tweets[followeeId]:
                tweet_lists.append(self.tweets[followeeId])
        
        # Merge k sorted linked lists to get top 10
        return self._mergeKLists(tweet_lists, 10)
    
    def _mergeKLists(self, lists, k):
        """Merge k sorted linked lists and return top k elements"""
        import heapq
        
        heap = []
        result = []
        
        # Initialize heap with head of each list
        for i, head in enumerate(lists):
            if head:
                # Use negative timestamp for max heap, and list index for tie-breaking
                heapq.heappush(heap, (-head.timestamp, i, head))
        
        # Extract top k elements
        while heap and len(result) < k:
            neg_timestamp, list_idx, node = heapq.heappop(heap)
            result.append(node.tweetId)
            
            # Add next node from the same list
            if node.next:
                heapq.heappush(heap, (-node.next.timestamp, list_idx, node.next))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)