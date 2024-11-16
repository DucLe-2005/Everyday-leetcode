class Solution {
    public boolean isPalindrome(String s) {
        
        
        char[] sArr = s.toCharArray();
        int l = 0;
        int r = sArr.length - 1;

        if (sArr.length < 1) {
            return false;
        }

        while (l < r) {
            while(l < r && ! Character.isLetterOrDigit(sArr[l])) {
                l++;
            }

            while (l < r && ! Character.isLetterOrDigit(sArr[r])) {
                r--;
            }

            if (Character.toLowerCase(sArr[l]) != Character.toLowerCase(sArr[r])) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
}