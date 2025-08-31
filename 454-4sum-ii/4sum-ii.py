from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = defaultdict(int)
        for a in nums1:
            for b in nums2:
                d[a+b] += 1
        
        count = 0
        for i in nums3:
            for j in nums4:
                if d[-(i + j)] > 0:
                    count += d[-(i + j)]
        
        return count


