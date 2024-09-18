class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initiate a stack of characters
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"} # hashmap of closing brackets to open

            
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]: # if closing bracket match open, pop them
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) # append opening bracket to stack
        
        return True if not stack else False

                 

                
        
        
        