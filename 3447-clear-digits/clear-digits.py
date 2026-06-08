class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        non_digits = []
        for i in range(len(s)):
            if s[i].isdigit():
                if non_digits:
                    s[i] = ""
                    s[non_digits.pop()] = ""
            else:
                non_digits.append(i)
        
        return "".join(s)
