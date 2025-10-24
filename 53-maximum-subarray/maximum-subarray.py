class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current sum is always positive
        # if current_sum + nums[i] < 0: reset current_sum = 0
        
        currentSum = 0
        maxSum = -float("inf")
        for n in nums:
            currentSum += n
            maxSum = max(maxSum, currentSum)
            if currentSum < 0:
                currentSum = 0

        return maxSum 