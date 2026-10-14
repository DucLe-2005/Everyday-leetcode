class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        x = max(math.floor(sum(nums) / len(nums)) + 1, 1)
        nums = set(nums)

        while x in nums:
            x += 1
        
        return x