class Solution(object):
    def majorityElement(self, nums):
        numCounts = {}

        for num in nums:
            if num in numCounts:
                numCounts[num] += 1
            else:
                numCounts[num] = 1
        
        for num in numCounts:
            if numCounts[num] > len(nums) / 2:
                return num
        
        return
