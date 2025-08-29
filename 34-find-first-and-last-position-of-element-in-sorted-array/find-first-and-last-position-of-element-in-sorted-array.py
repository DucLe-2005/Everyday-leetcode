class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if idx == -1:
            return [-1, -1]
        
        res = [-1, -1]
        l = r = idx
        
        while l >= 0:
            if nums[l] != target:
                break
            res[0] = l
            l -= 1
        
        while r < len(nums):
            if nums[r] != target:
                break
            res[1] = r
            r += 1
        
        return res
            