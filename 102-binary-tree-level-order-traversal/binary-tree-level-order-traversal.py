# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue: store the nodes in order
        # pop node from the queue
        # put the node's children into the queue
        # after finishing a level, add level's array of nodes to the result array
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                level.append(node.val)
            res.append(level)
        
        return res