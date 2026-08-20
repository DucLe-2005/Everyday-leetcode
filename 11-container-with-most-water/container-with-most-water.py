class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointers with left and right being the two sides of the container
        # update the volume of the container
        # move the pointer of lower height
        
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            volume = min(height[r], height[l]) * (r - l)
            res = max(res, volume)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res