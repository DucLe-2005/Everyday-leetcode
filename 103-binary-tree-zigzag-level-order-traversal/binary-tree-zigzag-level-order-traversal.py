# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        res = []
        left_to_right = True

        while q:
            size = len(q)
            vals = []

            for _ in range(size):
                node = q.popleft()
                vals.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if not left_to_right:
                vals.reverse()
            
            res.append(vals)
            left_to_right = not left_to_right

        return res
