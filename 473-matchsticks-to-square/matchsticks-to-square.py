class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # time: O(4^n)
        # space: O(n)
        if len(matchsticks) < 4:
            return False
        
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        target = total // 4
        
        # largest number cannot fit in any group
        if matchsticks[0] > target:
            return False

        buckets = [0, 0, 0, 0]

        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return True
            
            num = matchsticks[i]

            for j in range(4):
                if buckets[j] + num > target:
                    continue
                
                buckets[j] += num
                if dfs(i + 1):
                    return True
                buckets[j] -= num

            return False
        
        return dfs(0)
