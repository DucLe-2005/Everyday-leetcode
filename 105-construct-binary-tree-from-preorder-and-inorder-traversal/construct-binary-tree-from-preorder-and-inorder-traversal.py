# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, node in enumerate(inorder):
            inorder_map[node] = i
        
        preorder_idx = 0
        def build(l, r):
            nonlocal preorder_idx
            if l > r:
                return None
            
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
        
            root.left = build(l, inorder_map[root.val] - 1)
            root.right = build(inorder_map[root.val] + 1, r)

            return root
        
        return build(0, len(inorder) - 1)