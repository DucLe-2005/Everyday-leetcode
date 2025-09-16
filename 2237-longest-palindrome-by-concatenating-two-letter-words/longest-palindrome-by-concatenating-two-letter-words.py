class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words)
        res = 0
        middle = 0

        for w, f in d.items():
            reverse = w[::-1]

            if reverse == w:  # the word is palindrome itself
                if f % 2 == 0:
                    res += f * 2  # if frequency is even, spread the words evenly to 2 sides
                else:
                    res += (f - 1) * 2 # if odd, put one in the middle and spread the rest evenly
                    middle = 1
            elif w < reverse: # avoid double counting
                res += min(f, d[reverse]) * 4
        
        return res + middle * 2