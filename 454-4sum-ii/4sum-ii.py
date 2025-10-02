from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        val_map= defaultdict(int)
        n = len(nums1)
        res = 0
        for n1 in range(n):
            for n2 in range(n):
                val_map[nums1[n1] + nums2[n2]] += 1
        
        for n3 in range(n):
            for n4 in range(n):
                res += val_map[-nums3[n3] - nums4[n4]]

        return res

                    