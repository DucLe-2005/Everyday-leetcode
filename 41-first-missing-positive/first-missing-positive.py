class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        # Cycle sort numbers from 1 to n
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[correct_idx] != nums[i]:
                nums[correct_idx], nums[i] = nums[i], nums[correct_idx]
            else:
                i += 1
        # Return the first missing positive number in the sorted array        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1  # If 1 to n are present, n + 1 is the first missing positive number
        
        