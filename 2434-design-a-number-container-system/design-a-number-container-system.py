class NumberContainers:

    def __init__(self):
        self.index_map = {}
        self.number_map = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        # time: O(k), k = # of indexes that have number
        self.index_map[index] = number
        heapq.heappush(self.number_map[number], index)
        

    def find(self, number: int) -> int:
        # time: O(logk) amortized, O(klogk) worse-case for a call that removes stale indexes
        heap = self.number_map[number]

        while heap and self.index_map.get(heap[0]) != number:
            heapq.heappop(self.number_map[number])

        return heap[0] if heap else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)