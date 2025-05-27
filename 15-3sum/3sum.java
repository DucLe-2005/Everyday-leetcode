import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int a = nums[i];
            int l = i + 1;
            int r = nums.length - 1;

            while (l < r) {
                int curSum = a + nums[l] + nums[r];
                if (curSum > 0) {
                    r -= 1;
                } else if (curSum < 0) {
                    l += 1;
                } else {
                    res.add(Arrays.asList(a, nums[l], nums[r]));
                    l += 1;
                    while (nums[l] == nums[l-1] && l < r) {
                        l +=1;
                    }
                }
            }
        } 
        return res;
    }
}