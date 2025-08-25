class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_num = float("inf")
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if abs(target - closest_num) > abs(target - three_sum):
                    closest_num = three_sum
                
                if three_sum > target:
                    r -= 1
                elif three_sum < target:
                    l += 1
                else:
                    return closest_num
        
        return closest_num