class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep a running max and min product ending at index i
        # update the max and the min by getting the largest value and smallest value from the max * n, min * n, and n itself
        # update the result with current max at each step

        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            res = max(res, currMax)

        return res
            
