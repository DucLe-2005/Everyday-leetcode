# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        cur = dummy
        cur.next = head

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            
            cur.next = second
            first.next = second.next
            second.next = first
            cur = first

        return dummy.next
