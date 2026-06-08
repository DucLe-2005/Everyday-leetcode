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
        res = []
        max_count = 0
        for sum, count in sum_count.items():
            if count > max_count:
                max_count = count
                res = [sum]
            elif count == max_count:
                res.append(sum)
        
        return res