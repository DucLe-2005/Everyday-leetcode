class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1

        val = nums[0]
        k = 1

        for num in nums[1:]:
            if num != val:
                val = num
                nums[k] = num      
                k += 1
        
        return k
        