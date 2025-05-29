class Solution {
    public int maxArea(int[] height) {
        int res = 0;
        int l = 0;
        int r = height.length - 1;

        while (l < r ) {
            int maxArea = (r - l) * Math.min(height[r], height[l]);
            res = Math.max(maxArea, res);

            if (height[l] < height[r]) {
                l += 1;
            } else {
                r -= 1;
            }
        }

        return res;
    }
}