class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if candidate == num:
                count += 1
            elif count == 0:
                candidate = num
            else:
                count -= 1
        
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        
        if count > len(nums) / 2:
            return candidate
