# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])
        while q:
            val = 0
            count = len(q)
            for _ in range(len(q)):
                pop = q.popleft()
                val += pop.val
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            
            res.append(val / count)
        
        return res