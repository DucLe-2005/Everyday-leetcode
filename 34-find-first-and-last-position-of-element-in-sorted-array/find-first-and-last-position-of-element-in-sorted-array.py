class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]

        def lowerIndex():
            l, r = 0, len(nums) - 1

            while l <= r:
                m = (l + r) // 2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return l
        
        def upperIndex():
            l, r = 0, len(nums) - 1

            while l <= r:
                m = (l + r) // 2

                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            
            return r
        
        lower = lowerIndex()
        upper = upperIndex()

        if lower < 0 or lower >= len(nums) or upper >= len(nums) or nums[lower] != target:
            return [-1, -1]
        
        return [lower, upper]