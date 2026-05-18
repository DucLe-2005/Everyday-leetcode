class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if curr_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
            
        return res
