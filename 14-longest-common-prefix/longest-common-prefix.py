class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Binary search
        if not strs:
            return ""

        min_len = min(len(x) for x in strs)
        low = 0
        high = min_len
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][: (low + high) // 2]

    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True
