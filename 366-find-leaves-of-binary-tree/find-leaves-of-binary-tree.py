# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # time: O(n)
        # space: O(n)
        
        res = []
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            curr_height = max(left_height, right_height)

            if curr_height == len(res):
                res.append([])
            res[curr_height].append(node.val)
            
            return 1 + curr_height
        
        dfs(root)
        return res