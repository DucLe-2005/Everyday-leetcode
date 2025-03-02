class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        hash = {}
        for i,j in nums1:
            hash[i] = j
        
        for i, j in nums2:
            hash[i] = hash.get(i, 0) + j

        for i, j in hash.items():
            ans.append([i, j])

        return sorted(ans)
        