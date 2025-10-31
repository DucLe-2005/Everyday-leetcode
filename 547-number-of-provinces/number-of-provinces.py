class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

        def find(x):
            if self.parent[x] != x:
                self.parent[x] = find(self.parent[x])
            return self.parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return
            
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootX] = rootY
                self.rank[rootY] += 1


        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i, j)
        
        
        roots = {find(i) for i in self.parent}
        return len(roots)

        
    
    
