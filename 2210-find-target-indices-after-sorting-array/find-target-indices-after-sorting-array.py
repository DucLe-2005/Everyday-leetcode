class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = 0
        less_than = 0
        for n in nums:
            if n == target:
                count += 1
            if n < target:
                less_than += 1
        
        res = []
        for _ in range(count):
            res.append(less_than)
            less_than += 1

        return res
