class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        res = float("infinity")
        l = 0
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                res = min(res, r - l + 1)
                currentSum -= nums[l]
                l += 1
        
        return res if res != float("infinity") else 0

