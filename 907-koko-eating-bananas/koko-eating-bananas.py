class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time: O(n * log(k)), k = max(piles), n = len(piles)
        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = (low + high) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            
            if time <= h:
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        
        return res
