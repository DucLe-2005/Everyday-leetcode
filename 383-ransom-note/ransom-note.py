class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)

        for letter in ransomNote:
            if letter not in magazine_count or magazine_count[letter] == 0:
                return False
            else:
                magazine_count[letter] -= 1
        
        return True