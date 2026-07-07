class SeatManager:

    def __init__(self, n: int):
        self.seats = [x for x in range(1, n+1)] # min heap
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        # time: O(logn), n = # of seats
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        # time: O(logn)
        heapq.heappush(self.seats, seatNumber)       


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)