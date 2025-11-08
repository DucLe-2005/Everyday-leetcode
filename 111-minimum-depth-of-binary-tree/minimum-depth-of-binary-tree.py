# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = collections.deque([(root, 1)])

        while q:
            size = len(q)
            for _ in range(size):
                node, count = q.popleft()
                if not node.right and not node.left:
                    return count
                if node.left:
                    q.append((node.left, count + 1))
                if node.right:
                    q.append((node.right, count + 1))
