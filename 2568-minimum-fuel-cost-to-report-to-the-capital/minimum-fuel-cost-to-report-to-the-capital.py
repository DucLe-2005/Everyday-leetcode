class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # fuel based on number of cars passing each edge
        # number of cars = number of people / number of seats
        # time: O(n)
        # space: O(n)

        # build graph
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        self.fuel = 0

        def dfs(node, parent):
            people = 1

            for nei in graph[node]:
                if nei != parent:
                    people += dfs(nei, node)  
            
            self.fuel += math.ceil(people / seats)  
            
            return people

        
        for nei in graph[0]:
            dfs(nei, 0)
        
        return self.fuel


        