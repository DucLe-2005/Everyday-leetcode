class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 1:
            return path
        
        stack = []
        n = len(path)
        i = 0
        while i < n:

            if path[i] == "/":
                i += 1
                continue
            if path[i] == ".":
                if i + 1 == n: # . or .. at the end
                    break
                if path[i+1] == "/": # remove /.
                    i += 1 
                    continue
                
                if path[i+1] == ".":
                    if i + 2 == n or path[i+2] == "/":  # remove /..
                        i += 2
                        if stack:
                            stack.pop()
                        continue
                    
            curDir = ""
            while i < n and path[i] != "/":
                curDir += path[i]
                i += 1
            stack.append(curDir)

            i += 1
        
        return "/" + "/".join(stack)

            

