import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Hashtable<String, ArrayList<String>> res = new Hashtable<>();

        for (String str : strs) {
            int[] count = new int[26];
            for (char c: str.toCharArray()) {
                count[c - 'a']++;
            }

            // Use the letter counts as a signature key
            StringBuilder keyBuilder = new StringBuilder();
            for (int num : count) {
                keyBuilder.append(num).append('#');
            }
            String key = keyBuilder.toString();

            res.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(res.values());

    }
}