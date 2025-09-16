class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # use a hash table to count the sum of odd numbers of subarray ending at at each index
        # increase the count if 
            # a) there exists a prefix sum in hash table = k - nums[i]
            # b)prefix sum at index i = k
        
        prefix_sum = defaultdict(int)
        cur = 0
        res = 0
        for n in nums:
            if n % 2 != 0:
                cur += 1
            if cur == k:
                res += 1
            res += prefix_sum[cur - k]
            prefix_sum[cur] += 1

        return res  
            