class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # time: O(n)
        # space: O(n)
        num_set = set(nums)
        while original in num_set:
            original = 2 * original
        
        return original