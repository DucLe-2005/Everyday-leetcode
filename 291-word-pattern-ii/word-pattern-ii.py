class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.chars = list(pattern)
        self.words = list(s)
        word_to_ch = {}
        ch_to_word = {}
        
        def backtrack(c_index, w_index):
            if c_index == len(self.chars):
                return w_index == len(self.words)
            
            if w_index == len(self.words):
                return False

            c = self.chars[c_index]

            for end in range(w_index + 1, len(self.words) + 1):
                w = "".join(self.words[w_index:end])

                if c in ch_to_word and ch_to_word[c] != w:
                    continue
                if w in word_to_ch and word_to_ch[w] != c:
                    continue

                is_new_mapping = False
                if c not in ch_to_word:
                    word_to_ch[w] = c
                    ch_to_word[c] = w
                    is_new_mapping = True

                if backtrack(c_index + 1, end):
                    return True
                
                if is_new_mapping:
                    del ch_to_word[c]
                    del word_to_ch[w]

            return False

        return backtrack(0, 0)