class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x if x >= 0 else -x)
        return nums