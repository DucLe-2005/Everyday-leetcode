class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # time: O(k^n)
        # space: O(k + n)
        if len(nums) < k:
            return False
        
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False
        
        buckets = [0] * k

        def dfs(i: int) -> bool:
            if i == len(nums):
                return True
            
            num = nums[i]

            for j in range(k):
                if buckets[j] + num > target:
                    continue
                
                if j > 0 and buckets[j] == buckets[j-1]:
                    continue
                
                buckets[j] += num
                if dfs(i + 1):
                    return True
                buckets[j] -= num
            
            return False
        return dfs(0)