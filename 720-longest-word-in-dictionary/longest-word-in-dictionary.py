class Solution:
    def longestWord(self, words: List[str]) -> str:
        # put all words in a set
        # for each word, check if all their prefixes is in the set
        # if yes and len(word) > max length, update that word
        # if len(word) == max length, choose the word that is lexicographically smaller
        words = set(words)
        res = ""
        max_length = 0
        for word in words:
            is_valid = True
            print(f"word: {word}")
            for i in range(len(word) - 1, 0, -1):
                if word[:i] not in words:
                    print(f"{word[:i]} not in words")
                    is_valid = False
                    break
                
            if is_valid:
                if len(word) > max_length:
                    res = word
                    max_length = len(word)
                elif len(word) == max_length and word < res:
                    res = word
        
        return res