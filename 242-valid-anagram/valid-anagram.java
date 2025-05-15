import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        Hashtable<Character, Integer> charCount1 = new Hashtable<>();
        Hashtable<Character, Integer> charCount2 = new Hashtable<>();

        for (char c : s.toCharArray()) {
            if (charCount1.containsKey(c)) {
                charCount1.put(c, charCount1.get(c) + 1);
            }
            else {
                charCount1.put(c, 1);
            }
        }
        
        for (char c : t.toCharArray()) {
            if (charCount2.containsKey(c)) {
                charCount2.put(c, charCount2.get(c) + 1);
            } else {
                charCount2.put(c, 1);
            }
        }

        return charCount1.equals(charCount2);
    }
}