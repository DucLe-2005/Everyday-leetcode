class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        sentence = [""] * len(words)

        for word in words:
            sentence[int(word[-1]) - 1] = word[:-1]

        return " ".join(sentence) 