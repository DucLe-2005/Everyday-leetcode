# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if both left and right subtree have deepest nodes, return current node
        # if only one subtree has the deepest nodes, return that subtree
        def dfs(node):
            if not node:
                return (None, 0)
            
            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height == right_height:
                return (node, left_height+1)
            elif left_height > right_height:
                return (left_node, left_height+1)
            else:                
                return (right_node, right_height+1)
        
        return dfs(root)[0]