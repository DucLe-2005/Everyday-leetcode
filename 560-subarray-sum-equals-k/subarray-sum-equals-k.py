class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        all_sums = {0: 1} # sum: count
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            res += all_sums.get(prefix - k, 0)
            all_sums[prefix] = all_sums.get(prefix, 0) + 1
        
        return res