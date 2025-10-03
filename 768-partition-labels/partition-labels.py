class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # use two pointer to find the minimum substring that has all the occurences of the letter on the left
        # add to the hash map, letter: [start index, end index]
        # iterate the hash map, merge the intervals
        # return the length of each interval

        n = len(s)
        visited = set()
        letterSequence = []
        
        for i in range(n):
            if s[i] in visited:
                continue
            j = n - 1
            while i <= j and s[j] != s[i]:
                j -= 1
            visited.add(s[i])
            letterSequence.append([i, j])
        
        res = [letterSequence[0]]
        for start, end in letterSequence[1:]:
            prev_start, prev_end = res[-1]
            if start < prev_end:
                new_start = min(start, prev_start)
                new_end = max(end, prev_end)
                res[-1] = [new_start, new_end]
            else:
                res.append([start, end])
        
        return [end - start + 1 for start, end in res]


        
                        


        