class Solution:
    def reorganizeString(self, s: str) -> str:
        # time: O(nlogn)
        # space: O(n)
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        heap = []
        for c, frequency, in count.items():
            heapq.heappush(heap, (-frequency, c))
        
        prev_freq, prev_char = 0, None
        res = []
        while heap:
            curr_freq, curr_char = heapq.heappop(heap)
            res.append(curr_char)

            if prev_freq != 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = curr_freq + 1, curr_char
        
        return "".join(res) if len(res) == len(s) else ""