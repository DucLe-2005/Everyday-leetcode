class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.res = 0
        n = len(isConnected)

        def dfs(x, y):
            if not isConnected[x][y]:
                return
            
            isConnected[x][y] = 0

            for i in range(n):
                dfs(y, i)
            
            
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    dfs(i, j)
                    self.res += 1
        
        return self.res