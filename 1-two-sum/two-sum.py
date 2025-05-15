class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_table = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_table:
                return [num_table[diff], i]
            num_table[num] = i
        return None