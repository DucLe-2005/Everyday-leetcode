class SeatManager:

    def __init__(self, n: int):
        self.unreserved_seats = [x for x in range(1, n+1)] # min heap
        self.reserved_seats = set()

        heapq.heapify(self.unreserved_seats)

    def reserve(self) -> int:
        # time: O(logn), n = # of seats
        seat = heapq.heappop(self.unreserved_seats)
        self.reserved_seats.add(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        # time: O(logn)
        self.reserved_seats.remove(seatNumber)
        heapq.heappush(self.unreserved_seats, seatNumber)       


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)