class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        numCounts = {}

        for num in nums:
            if num in numCounts:
                numCounts[num] += 1
            else:
                numCounts[num] = 1
        
        for num in numCounts:
            if numCounts[num] > len(nums) / 3:
                res.append(num)
        
        return res

        