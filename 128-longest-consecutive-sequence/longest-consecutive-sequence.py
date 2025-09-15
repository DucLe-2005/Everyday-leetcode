class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:  # if this num is the first element, start counting
                length = 1
                while n + length in nums:
                    length += 1
                res = max(res, length)
        
        return res
