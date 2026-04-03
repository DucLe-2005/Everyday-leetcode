# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr:
            for _ in range(m):
                if not curr.next:
                    return dummy.next

                curr = curr.next

            next_node = curr.next
            for _ in range(n):
                if not next_node:
                    break

                next_node = next_node.next
            curr.next = next_node

        return dummy.next
        