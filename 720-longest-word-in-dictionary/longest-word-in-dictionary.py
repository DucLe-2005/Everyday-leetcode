class Solution:
    def longestWord(self, words: List[str]) -> str:
        # time: O(nlogn)
        # space: O(n)
        words.sort()
        best = ""
        valid = set()

        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)
                if len(word) > len(best) or len(word) == len(best) and word < best:
                    best = word
        
        return best