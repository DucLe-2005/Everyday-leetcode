class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.weight = [1.0] * n
    
    def find(self, x):
        if x != self.parent[x]:
            old_parent = self.parent[x]

            self.parent[x] = self.find(old_parent)
            self.weight[x] *= self.weight[old_parent]

        return self.parent[x]

    def union(self, a, b, value):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            a, b = b, a
            root_a, root_b = root_b, root_a
            value = 1 / value
        
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.weight[root_b] = self.weight[a] / value / self.weight[b]

        return True

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # e = len(equations), q = len(queries), n = # of variables
        # time: O(e * a(n) + q * a(n))
        # space: O(n)
        unique_var = list(set([item for e in equations for item in e]))
        variable = {}
        for i, var in enumerate(unique_var):
            variable[var] = i

        u = UnionFind(len(unique_var))

        for i, (a, b) in enumerate(equations):
            a_idx, b_idx = variable[a], variable[b]
            u.union(a_idx, b_idx, values[i])


        print(variable.items())
        res = []
        for a, b in queries:
            if a not in variable or b not in variable:
                res.append(-1.0)
                continue

            a_idx, b_idx = variable[a], variable[b]

            if u.find(a_idx) == u.find(b_idx):
                res.append(u.weight[a_idx] / u.weight[b_idx])
            else:
                res.append(-1.0)
        
        return res
