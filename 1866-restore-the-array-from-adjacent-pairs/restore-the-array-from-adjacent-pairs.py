class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        # time: O(n)
        # space: O(n)
        adj_map = defaultdict(list)
        for a, b in adjacentPairs:
            adj_map[a].append(b)
            adj_map[b].append(a)
        
        prev, curr = None, None
        for num in adj_map:
            if len(adj_map[num]) == 1:
                curr = num
                break
    
        res = []
        while len(res) < len(adj_map):
            res.append(curr)
            for nei in adj_map[curr]:
                if nei != prev:
                    prev, curr = curr, nei
                    break
             
        return res
            
            

