class Solution {
    public int maxSubArray(int[] nums) {
        int curSum = 0;
        int maxSum = nums[0];
        
        for (int num : nums) {
            if (num > (curSum + num)){
                curSum = num;
            } else {
                curSum += num;
            }
            if (curSum > maxSum) {
                maxSum = curSum;
            }
        }
          
        return maxSum;
    }
}
