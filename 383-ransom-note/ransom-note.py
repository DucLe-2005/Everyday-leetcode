class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = {}
        for c in magazine:
            magazineMap[c] = magazineMap.get(c, 0) + 1
        
        for d in ransomNote:
            if d not in magazineMap or magazineMap[d] == 0:
                return False
            else:
                magazineMap[d] -= 1
        
        return True
