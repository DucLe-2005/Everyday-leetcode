class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # time: O(m * nlogn + klog(sum(limits)))
        largest = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            row = [-x for x in grid[i]]
            heapq.heapify(row)

            for _ in range(limits[i]):
                largest.append(heapq.heappop(row))

        heapq.heapify(largest)
        res = 0
        for _ in range(k):
            res += -heapq.heappop(largest)

        return res