# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # if current node on root1 + current node on root2 < target:
        # do dfs on root2's right child  
        # if current node on root1 + current node on root > target:
        # do dfs on root2's left child
        # after reaching a leaf node on the second tree and still not find the correct pair:
        # recursively iterate the next node on the first tree and check recursively the nodes on the second tree
        # return true if a pair is found
        # return false at the end if no true is returned
        if not root1:
            return False
        
        if self.recurse_root_2(root1.val, root2, target):
            return True
        if root1.left and self.twoSumBSTs(root1.left, root2, target):
            return True
        if root1.right and  self.twoSumBSTs(root1.right, root2, target):
            return True
        
        return False

    def recurse_root_2(self, val: int, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        if val + root.val == target:
            return True
        
        if val + root.val < target:
            return self.recurse_root_2(val, root.right, target)
        else:
            return self.recurse_root_2(val, root.left, target)

