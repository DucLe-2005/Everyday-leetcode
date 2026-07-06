class StockPrice:

    def __init__(self):
        # lazy deletion with hash map and heaps
        self.records = defaultdict(int) # timestamp = price
        self.min_records = [] # min heap
        self.max_records = [] # max heap
        self.latest_timestamp = -1

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price
        heapq.heappush(self.min_records, (price, timestamp))
        heapq.heappush(self.max_records, (-price, timestamp))
        self.latest_timestamp = max(timestamp, self.latest_timestamp)

    def current(self) -> int:
        return self.records[self.latest_timestamp]

    def maximum(self) -> int:
        while self.max_records:
            price, timestamp = self.max_records[0]

            if self.records[timestamp] == -price:
                return -price

            heapq.heappop(self.max_records)

    def minimum(self) -> int:
        while self.min_records:
            price, timestamp = self.min_records[0]

            if self.records[timestamp] == price:
                return price

            heapq.heappop(self.min_records)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()