class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for i in range(len(nums)):
            left = prefix[i]
            right = prefix[-1] - prefix[i+1]

            if left == right:
                return i
        
        return -1

