class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = sorted(zip(timestamp, username, website))
        
        name_to_websites = defaultdict(list)
        for t, u, w in visits:
            name_to_websites[u].append(w)

        pattern_count = defaultdict(int)
        for name, websites in name_to_websites.items():
            if len(websites) < 3:
                continue

            seen = set()
            self.recordPattern(seen, name, websites, [], 0)

            for pat in seen:
                pattern_count[pat] += 1
        
        # Pick the highest count; break ties by lexicographically smallest pattern
        best_pat = None
        best_cnt = -1
        for pat, cnt in pattern_count.items():
            if cnt > best_cnt or (cnt == best_cnt and (best_pat is None or pat < best_pat)):
                best_pat = pat
                best_cnt = cnt

        return list(best_pat) if best_pat is not None else []
            
    def recordPattern(self, seen, name, websites, pattern, index):
        if len(pattern) == 3:
            seen.add(tuple(pattern))
            return

        for i in range(index, len(websites)):
            pattern.append(websites[i])
            self.recordPattern(seen, name, websites, pattern, i + 1)
            pattern.pop()
