class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        res = 0
        for w in words:
            reverse = w[::-1]
            if reverse in d and d[reverse] > 0:  # if the palindrome of the word exists, add to result
                d[reverse] -= 1
                res += 4
            else:
                d[w] += 1
        
        # add them middle value
        for n, val in d.items():
            if val > 0 and n[0] == n[1]:
                return res + 2
        
        return res