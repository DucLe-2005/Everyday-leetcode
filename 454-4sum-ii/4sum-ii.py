from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # count all sums from num1 and nums2
        d = defaultdict(int)
        for a in nums1:
            for b in nums2:
                d[a+b] += 1

        # count all how many complementary sums from nums3 and nums4 exist
        count = 0
        for i in nums3:
            for j in nums4:
                if -(i+j) in d:
                    count += d[-(i+j)]
        
        return count
