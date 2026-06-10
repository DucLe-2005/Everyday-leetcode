# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        curr = node.next
        while curr:
            prev.val = curr.val  
            curr = curr.next
            if not curr:
                prev.next = None
            prev = prev.next


        