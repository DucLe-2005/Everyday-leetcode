class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # time: O(n * m), n = # of words, m = # of letters in a word
        # space: O(n * m)
        chars = Counter(chars)
        res = 0
        for word in words:
            valid = True
            word_chars = Counter(word)
            for char, freq in word_chars.items():
                if char not in chars or chars[char] < freq:
                    valid = False
                    break
            
            if valid:
                res += len(word)
        
        return res