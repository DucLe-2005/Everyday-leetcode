class Solution:
    def longestDupSubstring(self, s: str) -> str:
        import random 

        n = len(s)
        nums = [ord(c) - ord('a') for c in s]  # Map chars to numbers

        # Base and mod for rolling hash
        base = random.randint(26, 100)
        mod = 2**63 - 1

        def search(length):
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod
        
            seen = {h}
            baseL = pow(base, length, mod)

            for start in range(1, n - length + 1):
                # Remove leftmost char, add new rightmost char
                h = (h * base - nums[start - 1] * baseL + nums[start + length - 1]) % mod
                if h in seen:
                    return start
                seen.add(h)
            return -1

        # Binary search for the longest length L
        l, r = 1, n
        start = -1
        max_len = 0

        while l <= r:
            mid = (l + r) // 2
            idx = search(mid)
            if idx != -1:  # Found a duplicate
                l = mid + 1
                start = idx
                max_len = mid
            else:
                r = mid - 1
        
        return s[start:start + max_len] if start != -1 else ""

