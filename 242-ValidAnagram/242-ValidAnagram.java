import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> countMap = new HashMap<>();

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        for (int i = 0; i < sArr.length; i++) {
            countMap.put(sArr[i], countMap.getOrDefault(sArr[i], 0) + 1);
            countMap.put(tArr[i], countMap.getOrDefault(tArr[i], 0) - 1);
        }
        for (int count : countMap.values()){
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
}