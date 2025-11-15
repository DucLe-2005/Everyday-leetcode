class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        found = [False] * (len(nums) + 1)
        for n in nums:
            found[n] = True
        
        res = []
        for i in range(1, len(nums) + 1):
            if not found[i]:
                res.append(i)
    
        return res