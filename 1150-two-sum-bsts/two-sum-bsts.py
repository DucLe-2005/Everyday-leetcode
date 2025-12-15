# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        set1, set2 = self.inorder(root1), self.inorder(root2)
        
        for num in set1:
            if (target - num) in set2:
                return True

        return False
    
    def inorder(self, root):
        res = set()

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            res.add(node.val)
            dfs(node.right)

        dfs(root)
        return res
            

        
        