class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == i + 1:
                continue
            
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp

        print(nums)
        
        res = []
        for i, num in enumerate(nums):
            if i + 1 != num:
                res.append(i + 1)
        
        return res