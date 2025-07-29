class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_1 = {}
        char_count_2 = {}

        for c in s:
            if c in char_count_1:
                char_count_1[c] += 1
            else:
                char_count_1[c] = 1
        
        for c in t:
            if c in char_count_2:
                char_count_2[c] += 1
            else:
                char_count_2[c] = 1

        return char_count_1 == char_count_2