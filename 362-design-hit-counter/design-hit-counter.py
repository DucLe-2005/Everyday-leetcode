class HitCounter:

    def __init__(self):
        self.total_hits = 0
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] + 1 > 300:
            self.queue.popleft()
            self.total_hits -= 1
        
        return self.total_hits

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)