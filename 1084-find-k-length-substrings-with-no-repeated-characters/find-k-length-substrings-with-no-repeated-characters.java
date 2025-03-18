class Solution {
    public int numKLenSubstrNoRepeats(String s, int k) {
        HashSet<Character> charSet = new HashSet<>();
        int ans = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            while (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left++;
            }

            charSet.add(s.charAt(right));

            ans = right - left + 1 >= k ? ans + 1 : ans;
        }

        return ans;
    }
}