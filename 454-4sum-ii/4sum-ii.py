from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # create a hash table to store occurences of sums made from nums1 and nums2
        # for all sums made from nums3 and nums4, check if (0 - num3 - num3) in the hash table
        # if yes, then add the value to result

        d = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                d[n1 + n2] += 1
        
        res = 0
        for n3 in nums3:
            for n4 in nums4:
                res += d[0 - n3 - n4]

        return res 