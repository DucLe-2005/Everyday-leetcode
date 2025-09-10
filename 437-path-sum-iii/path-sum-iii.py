# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        h = defaultdict(int)

        def preorder(node, currSum):
            if not node:
                return
            
            currSum += node.val
            # the current sum is the target sum
            if currSum == targetSum:
                self.count += 1
            # the path in between has the target sum
            self.count += h[currSum - targetSum]
            
            h[currSum] += 1
            preorder(node.left, currSum)
            preorder(node.right, currSum)
            h[currSum] -= 1
        
        preorder(root, 0)
        return self.count
