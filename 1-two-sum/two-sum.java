import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, Integer> numTable= new Hashtable<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (numTable.containsKey(diff))
                return new int[] {numTable.get(diff), i};
            numTable.put(nums[i], i);
        }
        return null;
    }
}