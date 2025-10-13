class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        self.prefixSum = 0
        for weight in w:
            self.prefixSum += weight
            self.prefixSums.append(self.prefixSum)
         
    def pickIndex(self) -> int:
        target = self.prefixSum * random.random()
        l, r = 0, len(self.prefixSums) - 1
        while l < r:
            m = (l + r) // 2
            if self.prefixSums[m] < target:
                l = m + 1
            else:
                r = m
        
        return l

            
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()