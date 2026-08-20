class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # time: O(n + i log i)
        # space: O(i)
        # n = number of items
        # i = number of unique student IDs
        scores = defaultdict(list)
        for student_id, score in items:
            heapq.heappush(scores[student_id], score)
            if len(scores[student_id]) > 5:
                heapq.heappop(scores[student_id])
        
        return sorted([[student_id, sum(top_scores) // 5] for student_id, top_scores in scores.items()])