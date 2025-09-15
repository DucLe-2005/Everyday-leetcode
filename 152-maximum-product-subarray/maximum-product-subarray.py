class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep a running max and min product ending at index i
        # when encounter 0, set the max and min product ending at index i to 1
        # update the result with current max at each step

        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            if n == 0:   # set max and min to 1 because 1 is neutral
                currMax, currMin = 1, 1
                continue
            
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            res = max(res, currMax)

        return res
            
