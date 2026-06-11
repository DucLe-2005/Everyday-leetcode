class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # pairs on the left start at even index while pairs on the right start at odd index
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            m = (r + l) // 2
            if m % 2 == 1:
                m -= 1
            
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m
        
        return nums[l]