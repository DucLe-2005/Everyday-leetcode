class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find_cross_subarray(nums, low, mid, high):
            left_sum = float("-inf")
            total = 0
            left_index = mid
            for i in range(mid, low -1, -1):
                total += nums[i]

                if total >= left_sum:
                    left_sum = total
                    left_index = i
            
            right_sum = float("-inf")
            total = 0
            right_index = mid + 1
            for i in range(mid + 1, high + 1):
                total += nums[i]
                
                if total >= right_sum:
                    right_sum = total
                    right_index = i
            
            return left_index, right_index, right_sum + left_sum




        def find_max_subarray(nums, low, high):
            if low == high:
                return [low, high, nums[low]]
            
            mid = (low + high) // 2

            left = find_max_subarray(nums, low, mid)
            right = find_max_subarray(nums, mid + 1, high)
            cross = find_cross_subarray(nums, low, mid, high)
            
            if left[2] >= right[2] and left[2] >= cross[2]:
                return left
            if right[2] >= left[2] and right[2] >= cross[2]:
                return right
            return cross

        return find_max_subarray(nums, 0, len(nums) - 1)[2]