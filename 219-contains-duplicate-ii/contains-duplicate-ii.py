class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = {}
        for r, num in enumerate(nums):
            if num in nums_map and abs(r - nums_map[num]) <= k:
                return True
            nums_map[num] = r
        
        return False