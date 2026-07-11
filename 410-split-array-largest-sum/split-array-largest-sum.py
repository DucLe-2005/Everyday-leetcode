class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # time: O(logn)
        # space: O(1)
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = (l + r) // 2

            parts = 1
            curr = 0
            for num in nums:
                if curr + num > m:
                    parts += 1
                    curr = num
                else:
                    curr += num

            # m is feasible
            if parts <= k:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
