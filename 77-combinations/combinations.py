class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(comb, start):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(comb, i + 1)
                comb.pop()
        
        backtrack([], 1)
        return res
    
    # time complexity: O(k * c(n, k))
    # space complexity: O()