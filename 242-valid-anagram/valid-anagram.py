class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_1 = {}
        char_count_2 = {}

        for num in s:
            if num in char_count_1:
                char_count_1[num] += 1
            else:
                char_count_1[num] = 1
        
        for num in t:
            if num in char_count_2:
                char_count_2[num] += 1
            else:
                char_count_2[num] = 1
        
        return char_count_1 == char_count_2