class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # time: O(nlogk), n = len(weights), k = (sum(weights), max(weights) is small and neglectable
        # space: O(1)
        low, high = max(weights), sum(weights)
        res = high
        while low <= high:
            mid = (low + high) // 2
            
            time = 1
            curr_capacity = 0
            for w in weights:
                if curr_capacity + w > mid:
                    curr_capacity = w
                    time += 1
                else:
                    curr_capacity += w

            if time <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res