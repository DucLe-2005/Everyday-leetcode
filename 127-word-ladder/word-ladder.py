class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        beginSet = {beginWord}
        endSet = {endWord}
        length = 1

        # bidirectional bfs from beginSet and endSet to find the shortest path
        while beginSet and endSet:
            if len(endSet) < len(beginSet):
                tmp = beginSet
                beginSet = endSet
                endSet = tmp
            
            newSet = set()
            for word in beginSet:
                neighbors = self.neighbors(word)
                for neighbor in neighbors:
                    if neighbor in endSet:
                        print(beginSet)
                        print(endSet)
                        return length + 1
                    if neighbor in words:
                        print(neighbor)
                        newSet.add(neighbor)
                        words.remove(neighbor)  # avoid cycle
            
            beginSet = newSet
            length += 1

        return 0  # we can't find a path between two words
        
    def neighbors(self, word):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        chars = list(word)
        res = []
        
        for i in range(len(word)):
            c = chars[i]
            for a in alphabet:
                chars[i] = a
                res.append("".join(chars))
            chars[i] = c
        
        return res