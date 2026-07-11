class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = self.move_left_pointer(0, len(nums) - 1, nums)
        r = self.move_right_pointer(l, len(nums) - 1, nums)
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            
            # left half is sorted
            if nums[m] >= nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = self.move_right_pointer(l, m - 1, nums)
                else:
                    l = self.move_left_pointer(l + 1, r, nums)
            # right half is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = self.move_left_pointer(l + 1, r, nums)
                else:
                    r = self.move_right_pointer(l, r - 1, nums)
        
        return False

    def move_left_pointer(self, l, r, nums):
        while l < r and nums[l] == nums[l+1]:
            l += 1
        
        return l
    
    def move_right_pointer(self, l , r, nums):
        while l < r and nums[r] == nums[r-1]:
            r -= 1
        
        return r