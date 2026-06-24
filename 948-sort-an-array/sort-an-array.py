class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            m = len(nums) // 2
            
            left = merge_sort(nums[:m])
            right = merge_sort(nums[m:])

            return merge(left, right)
        
        def merge(nums1, nums2):
            res = []
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
                
            
            res.extend(nums1[i:])
            res.extend(nums2[j:])
            
            return res
        
        return merge_sort(nums)