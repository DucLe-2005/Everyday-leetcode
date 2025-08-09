class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        }
        res = 0
        mask = 0
        mask_to_idx = [-1] * 32
        for i, c in enumerate(s):
            mask = mask ^ vowels.get(c, 0)
            if mask_to_idx[mask] != -1 or mask == 0:
                length = i - mask_to_idx[mask]
                res = max(res, length)
            else:
                mask_to_idx[mask] = i
        
        return res
