class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # hashmap to store the vowel count of each substring
        # slide window to check each substring
        curCount = 0
        maxCount = 0
        vowels = "aeiou"

        for i in range(k):
            if s[i] in vowels:
                curCount += 1

        maxCount = curCount
        l = 0
        r = k
        while r < len(s):
            # slide the right pointer by 1
            if s[r] in vowels:
                curCount += 1
            
            # slide the left pointer by 1
            if s[l] in vowels:
                curCount -= 1
            
            maxCount = max(curCount, maxCount)
            l += 1
            r += 1
        
        return maxCount