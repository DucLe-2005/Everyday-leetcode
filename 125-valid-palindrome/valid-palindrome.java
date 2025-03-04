class Solution {
    public boolean isPalindrome(String s) {
        return iterativeSolution(s);
    }

    boolean iterativeSolution(String s) {
        if (s.isEmpty()) {
            return true;
        }

        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            while(l < r && ! Character.isLetterOrDigit(s.charAt(l))) {
                l++;
            }

            while (l < r && ! Character.isLetterOrDigit(s.charAt(r))) {
                r--;
            }

            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }

        return true;

    }
}