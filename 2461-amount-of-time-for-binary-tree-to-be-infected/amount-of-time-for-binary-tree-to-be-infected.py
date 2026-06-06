# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # build an adjacency list
        # starting at 'start', bfs until there is no more nodes
        # record the bfs levels as the answer

        adjacency = defaultdict(list)

        def dfs(node):
            if node.left:
                adjacency[node.val].append(node.left.val)
                adjacency[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                adjacency[node.val].append(node.right.val)
                adjacency[node.right.val].append(node.val)
                dfs(node.right)
                
        dfs(root)
        res = 0
        visiting = set([start])
        q = deque([(start, 0)])
        while q:
            node, time = q.popleft()
            res = max(res, time)
            for nei in adjacency[node]:
                if nei in visiting:
                    continue
                visiting.add(nei)
                q.append((nei, time+1))

        return res