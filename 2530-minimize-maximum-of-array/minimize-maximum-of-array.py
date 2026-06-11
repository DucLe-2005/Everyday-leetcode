class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # x = min max num
        # prefix sum at i <= x * (i + 1)

        prefix_sum = nums.copy()  
        for i in range(1, len(nums)):
            prefix_sum[i] += prefix_sum[i-1]

        x = 0
        for i in range(len(prefix_sum)):
            x = max(x, math.ceil(prefix_sum[i] / (i+1)))
        
        return x