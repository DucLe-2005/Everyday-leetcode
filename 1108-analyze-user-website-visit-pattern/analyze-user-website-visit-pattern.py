class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = sorted(zip(timestamp, username, website))
        
        name_to_websites = defaultdict(list)
        for t, u, w in visits:
            name_to_websites[u].append(w)

        pattern_map = defaultdict(set)
        for name, websites in name_to_websites.items():
            if len(websites) < 3:
                continue
            
            self.recordPattern(pattern_map, name, websites, [], 0)
        
        sorted_patterns = sorted(pattern_map.items(), key=lambda x: (-len(x[1]), x[0]))
        return list(sorted_patterns[0][0])
            
        
    def recordPattern(self, pattern_map, name, websites, pattern, index):
        if len(pattern) == 3:
            print("add to pattern_map for", pattern, "for", name)
            pattern_map[tuple(pattern.copy())].add(name)
            return

        for i in range(index, len(websites)):
            pattern.append(websites[i])
            self.recordPattern(pattern_map, name, websites, pattern, i + 1)
            pattern.pop()
