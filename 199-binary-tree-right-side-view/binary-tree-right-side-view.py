# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # if not root:
        #     return []

        # self.res = []
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         pop = q.popleft()
        #         if i == 0:
        #             self.res.append(pop.val)
                
        #         if pop.right:
        #             q.append(pop.right)
        #         if pop.left:
        #             q.append(pop.left)
        
        # return self.res

        # DFS
        # 1. res = []
        # dfs(root, level)
        # if level > len(res): add root to result
        # 2. recursively traverse root -> right -> left
        # return res

        res = []
        def dfs(root, level):
            if not root:
                return
            if level > len(res):
                res.append(root.val)
            
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 1)
        return res




