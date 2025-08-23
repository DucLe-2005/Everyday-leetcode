class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) -1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if abs(target - three_sum) < abs(target - closest_sum):
                    closest_sum = three_sum

                if three_sum > target:
                    r -= 1
                elif three_sum < target:
                    l += 1
                else:  # exact match
                    return target

        return closest_sum