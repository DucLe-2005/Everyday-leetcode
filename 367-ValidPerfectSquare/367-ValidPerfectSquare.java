class Solution {
    public boolean isPerfectSquare(int num) {
        int l = 0;
        int r = num;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (mid * mid == num) {
                return true;
            } else if ((long) mid * mid > num) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return false;
    }
}