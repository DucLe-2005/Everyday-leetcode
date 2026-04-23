class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def dfs(i):
            if i == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()

            # skip duplicate numbers at the same recursion level
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1)
        
        dfs(0)
        return res