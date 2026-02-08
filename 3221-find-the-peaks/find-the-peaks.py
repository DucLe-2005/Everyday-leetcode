class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        curr_peak = 0
        new_peak = False
        for i in range(1, len(mountain)):
            if mountain[i] < mountain[i-1]:
                if new_peak:
                    res.append(curr_peak)
                    new_peak = False
            elif mountain[i] > mountain[i-1]:
                curr_peak = i
                new_peak = True
            else:
                new_peak = False
                
        return res
            