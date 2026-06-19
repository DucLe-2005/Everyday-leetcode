class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # prefix_sum = {sum: earliest index}
        # time: O(n)
        # space: O(n)

        nums = [num if num == 1 else -1 for num in nums]
        prefix_sum = {}
        prefix_sum[0] = 0
        curr_sum = 0
        res = 0

        for i, n in enumerate(nums):
            curr_sum += n
            if curr_sum == 0:
                print(f"res = {max(res, i + 1)}")
                res = max(res, i + 1)
                continue
            
            if curr_sum in prefix_sum:
                res = max(res, i - prefix_sum[curr_sum])

            # keep prefix sum with the earliest index
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum] = i
        
        return res
