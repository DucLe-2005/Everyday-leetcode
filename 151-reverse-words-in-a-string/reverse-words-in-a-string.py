class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. trim the string
        # 2. traverse each character
        # 3. record a word if a nonspace character is found and stops when a space is found
        # 4. append to result array
        # 5. reverse the result reverse and join the result array to a string
    
        s.strip()
        res = []
        index = 0
        
        while index < len(s):
            word = ""
            
            while index < len(s) and s[index] != " ":
                word += s[index]
                index += 1

            if word:
                res.append(word)

            index += 1
        
        return " ".join(res[::-1])