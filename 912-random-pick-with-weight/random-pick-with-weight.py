class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        self.prefixSum = 0
        for weight in w:
            self.prefixSum += weight
            self.prefixSums.append(self.prefixSum)
         
    def pickIndex(self) -> int:
        target = self.prefixSum * random.random()
        for i, prefixSum in enumerate(self.prefixSums):
            if target < prefixSum:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()