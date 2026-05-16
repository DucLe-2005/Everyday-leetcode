class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        min_heap = []

        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [x[1] for x in min_heap]

        # time: O(m logk), m = # of unique numbers
        # space: O(m + k)