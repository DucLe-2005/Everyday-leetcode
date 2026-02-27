class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
        
        if len(stones) > 0:
            return -stones[0]
        return 0