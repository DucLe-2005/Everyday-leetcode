from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for i, score in items:
            scores[i].append(score)
        
        res = []
        for x in sorted(scores.keys()):
            scores[x].sort(reverse=True)
            size = len(scores[x])
            top_five = scores[x][:5] if size > 5 else scores[x][:size]
            res.append([x, sum(top_five) // 5])
        
        return res
