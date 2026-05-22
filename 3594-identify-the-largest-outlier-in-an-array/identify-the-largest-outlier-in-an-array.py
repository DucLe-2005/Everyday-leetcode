class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(n)

        total = sum(nums)
        count = Counter(nums)
        res = -inf
        for num in nums:
            outlier = total - num * 2

            if outlier not in count:
                continue
            
            if outlier != num  or count[outlier] >= 2:
                res = max(res, outlier)
        
        return res