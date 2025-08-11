class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordCount = Counter(words)
        res = 0
        palindrome_in_middle = 0
        for w, freq in wordCount.items():
            s = w[::-1]
            if s == w:  # word is palindrome itself
                if freq % 2 == 0:  # if frequency is even, add them to both sides
                    res += freq * 2 
                else:  # if frequency is odd, add one palindrome in the middle
                    res += (freq - 1) * 2
                    palindrome_in_middle = 1
            elif w < s and s in wordCount:
                res += min(freq, wordCount[s]) * 4
        return res + palindrome_in_middle * 2