class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # time: O(n) (On log(3))
        # space: O(1)
        heap = []

        for char, frequency in [("a", a), ("b", b), ("c", c)]:
            if frequency > 0:
                heapq.heappush(heap, (-frequency, char))
        res = []
        
        while heap:
            curr_count, curr_char = heapq.heappop(heap)
            
            if len(res) >= 2 and res[-1] == res[-2] == curr_char:
                # a letter appears 3 times in a row
                if not heap:
                    break
                
                # Get the next most frequent char
                prev_char, prev_count = curr_char, curr_count
                curr_count, curr_char = heapq.heappop(heap)

                res.append(curr_char)
                curr_count += 1
                
                # Push 2 previously popped char back to heap
                if curr_count < 0:
                    heapq.heappush(heap, (curr_count, curr_char))
                heapq.heappush(heap, (prev_count, prev_char))
            else: # Add most frequent char to res
                res.append(curr_char)
                curr_count += 1
                if curr_count < 0:
                    heapq.heappush(heap, (curr_count, curr_char))
    
        return "".join(res)
