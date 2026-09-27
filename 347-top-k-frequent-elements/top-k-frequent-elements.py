class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        
        x = [(-count, num) for num, count in num_count.items()]
        heapq.heapify(x)

        res = []
        while k:
            _, num = heapq.heappop(x)
            res.append(num)
            k -= 1
        
        return res
            
            