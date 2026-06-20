class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = 0
        res = 0
        for n in nums:
            curr += n
            diff = curr - goal
            res += prefix[diff]
            prefix[curr] += 1
        
        return res
