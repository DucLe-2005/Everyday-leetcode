class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        beginSet = {beginWord}
        endSet = {endWord}
        length = 1

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                temp = beginSet
                beginSet = endSet
                endSet = temp
            newBeginSet = set()
            for word in beginSet:
                neighbors = self.neighbors(word)
                for neigh in neighbors:
                    if neigh in endSet:
                        return length + 1
                    if neigh in words:
                        words.remove(neigh)
                        newBeginSet.add(neigh)
            beginSet = newBeginSet
            length += 1
        
        return 0
    
    def neighbors(self, s: str) -> List[str]:
        chars = list(s)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for i in range(len(chars)):
            temp = chars[i]
            for a in alphabet:
                chars[i] = a
                res.append("".join(chars))
            chars[i] = temp
        return res
