class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        d = [0] * 61   # remainder -> count
        for t in time:
            r = t % 60
            res += d[60 - r]
            d[r if r else 60] += 1
        
        return res