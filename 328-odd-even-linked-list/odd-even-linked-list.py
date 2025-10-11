# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        evenStart = head.next
        odd, even = head, head.next

        while even.next and even.next.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        if odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
        
        even.next = None
        odd.next = evenStart
        
        return head
        
