# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return min([values[i] - values[i-1] for i in range(1, len(values))])