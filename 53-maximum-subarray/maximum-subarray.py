class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for n in nums[1:]:
            curSum = max(curSum, 0) + n
            maxSum = max(curSum, maxSum)
        
        return maxSum