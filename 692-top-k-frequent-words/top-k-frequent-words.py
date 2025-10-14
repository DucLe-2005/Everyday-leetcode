class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordMap = collections.defaultdict(int)
        for w in words:
            wordMap[w] += 1
        
        heap = []
        for word, freq in wordMap.items():
            heapq.heappush(heap, (-freq, word))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

