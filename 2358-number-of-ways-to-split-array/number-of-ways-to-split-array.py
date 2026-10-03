class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        left = 0 
        right = sum(nums)
        res = 0

        for i in range(len(nums) - 1):
            num = nums[i]
            left += num
            right -= num

            if left >= right:
                res += 1
        
        return res