class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        all_chars = set(''.join(words))
        graph = defaultdict(list)
        indegree = {c: 0 for c in all_chars}

        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            if len(word2) < len(word1) and word1.startswith(word2):
                return ""
            
            for j in range(len(word1)):
                if word1[j] != word2[j]:
                    if word1[j] in graph[word2[j]]:  # exit if detect a cycle
                        return ""
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1
                    break
        
        
        q = deque()
        for c, i in indegree.items():
            if i == 0:
                q.append(c)

        res = []
        while q:
            letter = q.popleft()
            if letter in res:
                return ""
            
            res.append(letter)
            for child in graph[letter]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        
        if len(res) != len(all_chars):
            return ""
        return "".join(res)

    # time: O(V + E), V = # of nodes, E = # of edges
    # space: O(V + E)