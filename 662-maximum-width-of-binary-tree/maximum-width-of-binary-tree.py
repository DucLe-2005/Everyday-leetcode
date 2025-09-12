# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        q = deque([(root, 0)])

        while q:
            n = len(q)
            _, first_idx = q[0]
            for i in range(n):
                node, idx = q.popleft()
                norm_idx = idx - first_idx  # get the idx at this level
                if node.left:
                    q.append((node.left, norm_idx * 2))
                if node.right:
                    q.append((node.right, norm_idx * 2 + 1))

                if i == n - 1:  # update max width when we reach the end of this level
                    max_width = max(max_width, norm_idx + 1)

        return max_width