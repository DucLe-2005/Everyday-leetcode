class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # count subarrays where num < right and where num < left

        def count(bound):
            res = 0
            cur = 0

            for num in nums:
                if num <= bound:
                    cur += 1
                else:
                    cur = 0
                
                res += cur
            
            return res
        
        return count(right) - count(left - 1)