class HitCounter:
    # queue: sums of hits in the recent 300 seconds
    # hit: add to queue, if number of hits exceed cap, pop hit in the front
    # getHits: return the sum

    def __init__(self):
        self.count = 0
        self.totalHits = 0
        self.currentHits = 0
        self.currentTime = 0
        self.queue = collections.deque()  # (number of hits, timestamp)
        

    def hit(self, timestamp: int) -> None:
        if self.currentTime == timestamp:
            self.currentHits += 1
            self.totalHits += 1
        else:
            self.queue.append((self.currentHits, self.currentTime))

            self.totalHits += 1
            self.currentTime = timestamp
            self.currentHits = 1

            self._prune(timestamp)
            

    def getHits(self, timestamp: int) -> int:
        if timestamp > self.currentTime:
            self.queue.append((self.currentHits, self.currentTime))
            self.currentHits = 0
        self.currentTime = timestamp
        self._prune(timestamp)
        return self.totalHits
    
    def _prune(self, now):
        while self.queue and now - self.queue[0][1] >= 300:
                hits, t = self.queue.popleft()
                self.totalHits -= hits


            
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)