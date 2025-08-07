class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i):
            if i == len(nums):
                res.append(cur[:])
                return
            
            # include nums[i]
            cur.append(nums[i])
            dfs(i + 1)

            # exclude nums[i]
            cur.pop()
            dfs(i + 1)

        dfs(0)
        
        return res



        
    
    # time complexity: O(n * 2^n)
    # space complexity: O(n *2^n) total, O(n) stack
