# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                pop = q.popleft()
                row.append(pop.val)
                if pop.right:
                    q.append(pop.right)
                if pop.left:
                    q.append(pop.left)
            row.reverse()
            res.append(row)

        res.reverse()
        return res
            