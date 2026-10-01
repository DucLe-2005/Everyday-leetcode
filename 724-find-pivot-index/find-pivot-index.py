class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        left_prefix = [nums[0]]
        for num in nums[1:]:
            left_prefix.append(left_prefix[-1] + num)
        
        right_prefix = [0] * (n)
        right_prefix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_prefix[i] = right_prefix[i+1] + nums[i]

        print(left_prefix)
        print(right_prefix)
        for i in range(n):
            left_sum = left_prefix[i-1] if i - 1 >= 0 else 0
            right_sum = right_prefix[i+1] if i + 1 < n else 0
            
            if left_sum == right_sum:
                return i
        return -1
        

