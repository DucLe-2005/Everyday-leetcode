class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        long l = 1;
        long r = Arrays.stream(piles).max().getAsInt();
        long res = r;
        while (l <= r) {
            long mid = (l + r) / 2;
            long hours = 0;
            for (int pile : piles) {
                hours += (int) Math.ceil((double) pile / mid);
            }

            if (hours <= h) {
                res = Math.min(res, mid);
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return (int) res;
    }
}