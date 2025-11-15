class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_to_word = defaultdict(list)
        word_to_letter = defaultdict(list)
        words = s.split(" ")  
        letters = list(pattern)


        if len(words) != len(letters):
            return False
        
        for i in range(len(words)):
            if letters[i] in letter_to_word or words[i] in word_to_letter:
                if (letter_to_word[letters[i]] != words[i] or
                    word_to_letter[words[i]] != letters[i]):
                    return False
            letter_to_word[letters[i]] = words[i]
            word_to_letter[words[i]] = letters[i]

        return True
