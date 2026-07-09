class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if nums[l] <= nums[r]: sorted window
        # move l = m + 1 if nums[m] < target else r = m - 1


        # unsorted window
        # if m on left and m < target: l = m + 1
        # if m on left and m > target and target > l: r - m - 1
        # if m on left and m > target and target < l: l = m + 1

        # if m on right and m > target: r = m - 1
        # if m on right and m < target and target < r: l = m + 1
        # if m on right and m < target and target > r: r = m - 1
        

        l, r = 0, len(nums) - 1
        i = 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # sorted window
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                
            # unsorted window
            else:
                # m is on left portion
                if nums[m] >= nums[l]:
                    if nums[m] < target or target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                # m is on right portion
                else:
                    if nums[m] > target or target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
            i += 1
        
        return -1