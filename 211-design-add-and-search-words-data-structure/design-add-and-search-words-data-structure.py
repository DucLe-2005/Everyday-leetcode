class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                return root.is_end
            
            print(word[i])
            if word[i] == ".":
                for child in root.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            if word[i] not in root.children:
                return False
            
            return dfs(root.children[word[i]], i+1)

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)