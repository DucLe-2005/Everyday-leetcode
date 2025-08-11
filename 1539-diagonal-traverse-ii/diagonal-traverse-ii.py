class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i+j].append(nums[i][j])
        
        res = []
        for values in diagonals.values():
            for n in values[::-1]:
                res.append(n)
        
        return res

