# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build_tree(l, r):
            if l > r:
                return None
            
            m = (l + r) // 2
            root = TreeNode(values[m])
            root.left = build_tree(l, m - 1)
            root.right = build_tree(m + 1, r)  

            return root
        
        return build_tree(0, len(values) - 1)
