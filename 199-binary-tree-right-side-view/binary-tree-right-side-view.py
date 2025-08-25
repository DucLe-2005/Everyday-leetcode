# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        def preorder(node, level):
            if len(res) == level:
                res.append(node.val)
            
            if node.right:
                preorder(node.right, level + 1)
            if node.left:
                preorder(node.left, level + 1)
            
        preorder(root, 0)
        return res