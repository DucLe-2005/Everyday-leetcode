class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        if len(mountain) < 3:
            return []
        
        res = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                res.append(i)
        
        return res
            