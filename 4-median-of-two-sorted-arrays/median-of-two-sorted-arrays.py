class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # use binary search to cut parition on the shorter list
        # time: O(log(min(m, n))
        # space: O(1)
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        l, r = -1, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i  - 2 # B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Bright, Aright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright: # left paritition of A is too much
                r = i - 1
            else: # left partition of B is too much
                l = i + 1


