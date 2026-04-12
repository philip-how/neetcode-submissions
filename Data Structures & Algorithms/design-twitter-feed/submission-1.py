import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.followers = {}
        self.posts = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
            self.following[userId] = {userId}
            self.followers[userId] = {userId}
        
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNthLastPost(self, userId, n):
        if len(self.posts[userId]) <= n:
            return
        return (self.posts[userId][-(n+1)][0], self.posts[userId][-(n+1)][1], userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        following_ls = []
        index_up_to = {}
        for user_following in self.following[userId]:
            nthPost = self.getNthLastPost(user_following, 0)
            index_up_to[user_following] = 0
            if nthPost is not None:
                following_ls.append(nthPost)
        
        heapq.heapify_max(following_ls)

        feed = []
        for i in range(10):
            if len(following_ls) == 0:
                return feed
            
            timestamp, tweetId, poster = heapq.heappop_max(following_ls)

            feed.append(tweetId)

            index_up_to[poster] += 1

            new_post = self.getNthLastPost(poster, index_up_to[poster])

            if new_post is not None:
                heapq.heappush_max(following_ls, new_post)
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        for userId in (followerId, followeeId):
            if userId not in self.posts:
                self.posts[userId] = []
                self.following[userId] = {userId}
                self.followers[userId] = {userId}
        
        self.followers[followeeId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers[followeeId]:
            return
        
        if followerId == followeeId:
            return
        
        self.followers[followeeId].remove(followerId)
        self.following[followerId].remove(followeeId)

        return
