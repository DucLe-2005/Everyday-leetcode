class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # num: index
        for i, num in enumerate(nums):
            if target - num in num_map:
                return [i, num_map[target - num]]
            num_map[num] = i
        return []