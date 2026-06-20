class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # a % k = 0: return True
        # a % k = c and b % k = c, so (a - b) % c == 0

        prefix = {} # remainder: index
        prefix[0] = -1
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum += n
            r = curr_sum % k
            if r in prefix:
                if i - prefix[r] >= 2:
                    return True
            else:
                prefix[r] = i
    
        return False
        