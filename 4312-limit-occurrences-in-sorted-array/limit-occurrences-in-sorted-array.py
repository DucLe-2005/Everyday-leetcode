class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        count = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                count = 1
                res.append(nums[i])
            else:
                count += 1
                if count > k:
                    continue
                res.append(nums[i])
        
        return res
