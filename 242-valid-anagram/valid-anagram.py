class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        
        return len(count) == 0
    
        # time: O(s + t)
        # space: O(s)
