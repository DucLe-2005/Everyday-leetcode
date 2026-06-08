# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_count = {}

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            sum = left + right + node.val
            sum_count[sum] = sum_count.get(sum, 0) + 1

            return sum
        
        dfs(root)
        max_freq = max(sum_count.values())
        return [s for s in sum_count if sum_count[s] == max_freq]