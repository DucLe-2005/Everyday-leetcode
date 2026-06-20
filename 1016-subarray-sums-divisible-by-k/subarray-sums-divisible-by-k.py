class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # prefix[sum] = count
        # a % k = b
        # (a - b) % k == 0
        # -> find b; res += prefix[b]
        # time: O(n)
        # space: O(k)

        prefix = defaultdict(int)
        prefix[0] = 1
        curr_sum = 0
        res = 0
        for i, n in enumerate(nums):
            curr_sum += n
            remainder = curr_sum % k
            
            print(f"sum: {curr_sum}, remainder: {remainder}, idx: {i}")
            print(f"res += {prefix[remainder]}, prefix[{remainder}] = {prefix[remainder]}")
            res += prefix[remainder]
            prefix[remainder] += 1
        
        return res
