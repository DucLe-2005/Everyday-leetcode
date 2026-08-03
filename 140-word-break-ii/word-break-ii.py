class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # time: O(W + n * 2^n), n = len(s), W = sum of letters in wordDict
        # space: O(W + n)
        root = self.buildTrieDict(wordDict)
        res = []

        def dfs(i, node, path, curr_word):
            if i == len(s) - 1:
                if node.is_end:
                    path.append(curr_word)
                    res.append(" ".join(path))
                    path.pop()
                return

            letter = s[i+1]
            if letter not in node.children:
                return
            
            child = node.children[letter]
            if child.is_end:
                path.append(curr_word + letter)
                dfs(i+1, root, path, "")
                path.pop()
                
            dfs(i+1, child, path, curr_word + letter)
                    
        if s[0] in root.children:
            node = root.children[s[0]]
            if node.is_end:
                dfs(0, root, [s[0]], "")
            dfs(0, node, [], s[0])

        return res
                
    
    def buildTrieDict(self, wordDict: List[str]) -> Node:
        root = Node()
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Node()
                curr = curr.children[ch]
            curr.is_end = True
        
        return root