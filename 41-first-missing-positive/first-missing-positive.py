class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Convert negative numbers to 0
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1
        
        # Turn the ints at the indexes to negative
        # if numbers from 1 to len(nums) are present in nums
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1
