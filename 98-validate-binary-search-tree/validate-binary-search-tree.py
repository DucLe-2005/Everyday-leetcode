# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, upper, lower):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return isValid(root.left, root.val, lower) and isValid(root.right, upper, root.val)
        
        return isValid(root, float("inf"), -float("inf"))
        
        