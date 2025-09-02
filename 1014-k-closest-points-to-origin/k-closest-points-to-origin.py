class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([x**2 + y**2, x, y])

        heapq.heapify(distances)
        res = []
        for _ in range(k):
            dis, x, y = heapq.heappop(distances)
            res.append([x, y])
        
        return res
        