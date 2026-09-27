class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        word_count = defaultdict(int)
        for w in words:
            word_count[w] += 1
        
        word_list = [(-count, word) for word, count in word_count.items()]
        heapq.heapify(word_list)

        res = []
        while k:
            res.append(heapq.heappop(word_list)[1])
            k -= 1
        
        return res