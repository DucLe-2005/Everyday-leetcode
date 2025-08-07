class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)

        def backtrack(subset, start):
            if start == n:
                return
            
            for i in range(start, n):
                subset.append(nums[i])
                res.append(subset.copy())
                backtrack(subset, i + 1)
                subset.pop()
        
        backtrack([], 0)
        return res
    
    # time complexity: O(k * 2^n)
    # space complexity: 
