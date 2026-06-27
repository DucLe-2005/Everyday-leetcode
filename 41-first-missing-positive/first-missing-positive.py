class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1. cycle sort nums
        # if num in [1,n]: put them in index (num - 1)
        # else: skip
        # the firt number that val != index + 1 is the missing smallest positive integer
        
        # cycle sort nums
        n = len(nums)
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 <= correct_idx < n and nums[correct_idx] != nums[i]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        # find the first number that is not in the right order
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1