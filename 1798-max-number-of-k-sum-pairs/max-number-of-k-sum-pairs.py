class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        visited = {}
        for num in nums:
            if k - num in visited:
                visited[k - num] -= 1
                if visited[k - num] == 0:
                    del visited[k - num]
                res += 1
            else:
                visited[num] = visited.get(num, 0) + 1
        
        return res