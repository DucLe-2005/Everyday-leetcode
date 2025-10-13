class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        currentString = []
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                countStack.append(k)
                stringStack.append(currentString)
                currentString = []
                k = 0
            elif c == ']':
                repeat = countStack.pop()
                currentString = stringStack.pop() + currentString * repeat
            else:
                currentString.append(c)
        
        return "".join(currentString)
        

                    


