class HitCounter:

    def __init__(self):
        self.total_hits = 0
        self.queue = deque()
        self.current_time = 0

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        self.total_hits += 1
        self.current_time = timestamp
        self._updateHits()

    def getHits(self, timestamp: int) -> int:
        self.current_time = timestamp
        self._updateHits()
        return self.total_hits
    
    def _updateHits(self) -> None:
        while self.queue and self.current_time - self.queue[0] + 1 > 300:
            self.queue.popleft()
            self.total_hits -= 1



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)