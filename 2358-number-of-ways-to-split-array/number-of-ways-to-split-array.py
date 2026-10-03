class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(prefix[-1] + num)
        
        res = 0
        for i in range(len(prefix) - 1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                res += 1
        
        return res