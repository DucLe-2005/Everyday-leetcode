class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = 0
        res = 0
        for n in nums:
            curr += n
            diff = curr - goal
            
            print(f"n: {n}, sum: {curr}, prefix[{diff}]: {prefix[diff]}")
            res += prefix[diff]
            print(f"res = {res}")
            prefix[curr] += 1
        
        return res
