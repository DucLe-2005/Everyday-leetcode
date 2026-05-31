class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_num, max_num = min(nums), max(nums)
        nums = set(nums)
        res = []
        for i in range(min_num + 1, max_num):
            if i not in nums:
                res.append(i)
        
        return res