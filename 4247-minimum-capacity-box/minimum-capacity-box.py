class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = -1
        min_capacity = inf
        for i in range(len(capacity) -1, -1, -1):
            if capacity[i] >= itemSize and capacity[i] <= min_capacity:
                min_capacity = capacity[i]
                res = i
        
        return res