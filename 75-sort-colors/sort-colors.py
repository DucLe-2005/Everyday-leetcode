class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        def swap(a, b):
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1