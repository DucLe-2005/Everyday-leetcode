class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        current_end = 0
        farthest = 0
        jumps = 0

        for i in range(n - 1):  # don't make another jump at the last index
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                current_end = farthest
                jumps += 1
            
            if current_end == n - 1:
                break
            
        return jumps

