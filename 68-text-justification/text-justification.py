class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # pack as many words to a line as possible
        # at least one space between words ( 3 words + 2 spaces)
        # if spaces are uneven, distribute more space to the leftmost slot
        # last line is left justified.


        # iterate words, add up the width
        # if current width is larger or equal to maxWidth, add the sentence
        # if there's only one word, left justify the sentence
        # if there are more words, calculate the number of spaces that can be distributed to the slots
        # if there are off # of spaces, the left slots gets more spaces
        # add the last sentence left justified
        res = []
        line, line_chars = [], 0

        def justify(line_words, line_chars, is_last):
            # Single word or last word: left justify
            if is_last or len(line_words) == 1:
                s = " ".join(line_words)
                return s + " " * (maxWidth - len(s))

            gaps = len(line_words) - 1
            extra = maxWidth - line_chars
            q, r = divmod(extra, gaps)

            parts = []
            for i, w in enumerate(line_words[:-1]): # Don't add space to right of last word
                spaces = q + (1 if i < r else 0)
                parts.append(w + " " * spaces)
            
            parts.append(line_words[-1])
            
            return "".join(parts)


        for w in words:
            if line and line_chars + len(w) + len(line) > maxWidth: # if adding this word + chars already in the line overflow, plush the current line
                res.append(justify(line, line_chars, is_last = False))
                line, line_chars = [], 0

            line.append(w)
            line_chars += len(w)
        
        # Flush last line: left justified
        res.append(justify(line, line_chars, is_last = True))
        return res
        



            

