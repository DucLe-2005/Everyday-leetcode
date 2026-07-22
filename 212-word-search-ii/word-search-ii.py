class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct a trie
        # for each cell, check if the cell exists in node.children
        # if yes, dfs to that cell, node = node.children[cell]
        # if node.is_end = True, add word
        rows, cols = len(board), len(board[0])
        visited = set()
        trie = self.makeTrie(words)
        res = set()

        def dfs(r: int, c: int, node: Node, letters: [str]) -> None:
            if node.is_end:
                res.add("".join(letters))
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            letters.append(board[r][c])
            next_node = node.children[board[r][c]]
            dfs(r + 1, c, next_node, letters)
            dfs(r - 1, c, next_node, letters)
            dfs(r, c + 1, next_node, letters)
            dfs(r, c - 1, next_node, letters)

            visited.remove((r, c))
            letters.pop()

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie, [])
        return list(res)

    def makeTrie(self, words: List[str]) -> Node | None:
        root = Node()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.is_end = True
        
        return root
