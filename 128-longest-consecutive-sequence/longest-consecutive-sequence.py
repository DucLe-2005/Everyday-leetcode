class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(n)

        res = 0
        nums = set(nums)  
        for n in nums:
            if n - 1 in nums:
                continue
            length = 1
            while n + length in nums:
                length += 1
            res = max(res, length)
        
        return res