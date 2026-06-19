class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        curr_prefix = 0
        prefix_sum[0] = 1
        res = 0
        for n in nums:
            curr_prefix += n
            diff = curr_prefix - k
            res += prefix_sum[diff]
            prefix_sum[curr_prefix] += 1
        
        return res