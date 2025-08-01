class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int i = m + n - 1;
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[i] = nums1[p1];
                p1 -= 1;
            } else {
                nums1[i] = nums2[p2];
                p2 -= 1;
            }
            i -= 1;
        }

        if (p2 >= 0) {
            for (int c = 0; c <= p2; c++) {
                nums1[c] = nums2[c];
            }
        }
    }
}