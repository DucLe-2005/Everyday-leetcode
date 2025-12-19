class Solution(object):
    def removeDuplicates(self, nums):
        val = None
        k = 0

        for num in nums:
            if num != val:
                val = num
                nums[k] = num      
                k += 1
        
        return k
        