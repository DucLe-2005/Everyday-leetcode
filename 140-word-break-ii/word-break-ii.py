class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # construct a trie word dictionary
        # at index ith, if s[i] is end of a word in wordDict, add the word to the path
        # if i == len(s): add path to result
        # travel dfs(node.childrens[i])
        root = self.buildTrieDict(wordDict)
        res = []

        def dfs(i, node, path, curr_word):
            if i == len(s) - 1:
                if node.is_end:
                    path.append(curr_word)
                    res.append(" ".join(path))
                    path.pop()
                return

            for letter, child in node.children.items():
                if letter == s[i+1]:
                    if child.is_end:
                        print(f"letter: {letter}, word: {curr_word}")
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