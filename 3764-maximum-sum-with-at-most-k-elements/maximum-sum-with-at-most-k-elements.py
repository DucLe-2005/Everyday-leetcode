import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if k == 0:
            return 0

        min_heap = []

        for i, row in enumerate(grid):
            row.sort(reverse=True)

            for num in row[:limits[i]]:
                if len(min_heap) < k:
                    heapq.heappush(min_heap, num)
                elif num > min_heap[0]:
                    heapq.heapreplace(min_heap, num)

        return sum(min_heap)