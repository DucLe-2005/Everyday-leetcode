# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    # init:
    # time: O(n)
    # space: O(n)

    # find:
    # time: O(1)
    # space: O(1)
    def __init__(self, root: Optional[TreeNode]):
        self.element_set = set([0])
        
        def recover(root, val):
            if not root:
                return
            
            if root.left:
                left = val * 2 + 1
                self.element_set.add(left)
                recover(root.left, left)
            if root.right:
                right = val * 2 + 2
                self.element_set.add(right)
                recover(root.right, right)
        
        recover(root, 0)
        
    def find(self, target: int) -> bool:
        return target in self.element_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)