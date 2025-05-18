import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        ArrayList<Integer>[] freq = new ArrayList[nums.length + 1];
        HashMap<Integer, Integer> count = new HashMap<>();

        // Count frequencies
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Initialize each bucket
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        // Place numbers into frequency buckets
        count.forEach((n, c) -> {
            freq[c].add(n);
        });

        int[] res = new int[k];
        int idx = 0;

        // Traverse buckets from high frequency to low
        for (int i = freq.length - 1; i >= 0 && idx < k; i--) {
            for (int n : freq[i]) {
                res[idx++] = n;
                if (idx == k) {
                    return res;
                }
            }
        }

        return res; // in case k == 0 or other edge case
    }
}
