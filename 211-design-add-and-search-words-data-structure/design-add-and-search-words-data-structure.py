class Node:
    def __init__(self):
        self.children: [str, Node()] = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end

            ch = word[i]

            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(i + 1, node.children[ch])

        return dfs(0, self.root)
