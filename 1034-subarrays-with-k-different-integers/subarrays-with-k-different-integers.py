class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithAtMostK(nums, k) - self.subarraysWithAtMostK(nums, k - 1)

    def subarraysWithAtMostK(self, nums, k):
        count = 0
        countMap = {}
        distinct = 0
        l, r = 0, 0

        while l <= r and r < len(nums):
            if nums[r] not in countMap:
                countMap[nums[r]] = 1
                distinct += 1
            else:
                countMap[nums[r]] += 1
            
            while distinct > k:
                countMap[nums[l]] -= 1
                if countMap[nums[l]] == 0:
                    del countMap[nums[l]]
                    distinct -= 1
                l += 1
            
            r += 1
            count += r - l + 1
        
        return count

                

