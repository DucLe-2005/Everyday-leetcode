class Solution:
    def longestPalindrome(self, s: str) -> int:
        wordCount = Counter(s)
        middle = 0
        res = 0
        for letter, count  in wordCount.items():
            if count % 2 == 0:
                res += count
            else:
                if not middle:
                    middle = 1
                res += count - 1
        
        return res + middle