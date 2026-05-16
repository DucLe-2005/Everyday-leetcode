class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time: O(n)
        # space: O(1)
        res = [1 for _ in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res        