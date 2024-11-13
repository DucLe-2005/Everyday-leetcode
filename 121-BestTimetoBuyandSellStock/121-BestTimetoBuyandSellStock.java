class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }


        int l = 0, r = 1, maxP = 0;
        while (l < prices.length - 1 && r < prices.length) {
            if (prices[r] > prices[l]) {
                int profit = prices[r] - prices[l];
                if (profit > maxP) {
                    maxP = profit;
                }
            } else {
                l = r;
            }
            r++;
        }
        return maxP;
    }
}