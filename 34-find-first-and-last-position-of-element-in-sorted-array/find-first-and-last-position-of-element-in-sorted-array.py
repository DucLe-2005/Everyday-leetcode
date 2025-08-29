class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def upper_bound(x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= x:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        i = lower_bound(target)
        if i == len(nums) or nums[i] != target:
            return [-1, -1]
        
        j = upper_bound(target)
        return [i, j - 1]
