class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(n)

        prefix_sum = {}
        prefix_sum[0] = -1
        curr_sum = 0
        res = 0

        for i, n in enumerate(nums):
            curr_sum += n if n == 1 else -1

            if curr_sum in prefix_sum:
                res = max(res, i - prefix_sum[curr_sum])
            else:
                prefix_sum[curr_sum] = i

        return res