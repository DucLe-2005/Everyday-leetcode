class HitCounter:

    def __init__(self):
        self.count = 0
        self.current_time = 0
        self.past_hits = deque()

    def hit(self, timestamp: int) -> None:
        self.past_hits.append(timestamp)
        self.current_time = timestamp
        self.count += 1
        self.update_queue()

    def getHits(self, timestamp: int) -> int:
        self.current_time = timestamp
        self.update_queue()
        return self.count
    
    def update_queue(self):
        print("current time", self.current_time)
        print(self.past_hits)
        while (
            self.past_hits and
            self.current_time - self.past_hits[0] >= 300
            ):
            print("pop:", self.past_hits[0])
            self.count -= 1
            self.past_hits.popleft() 


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)