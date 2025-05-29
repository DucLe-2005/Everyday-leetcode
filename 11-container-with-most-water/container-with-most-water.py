class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE SOLUTION
        # res = 0
        
        # for i in range(len(height)):
        #     for j in range(i+1, len(height), 1):
        #         max_area = (j - i) * min(height[i], height[j])
        #         res = max(max_area, res)
        # return res

        # TWO POINTERS SOLUTION
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            max_area = (r - l) * min(height[r], height[l])
            res = max(max_area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res
