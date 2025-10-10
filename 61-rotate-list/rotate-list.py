# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # close the linked list into the ring
        n = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        
        if k % n == 0:
            return head
        
        old_tail.next = head

        # find new tail: (n - k % n -1)
        # find new head: (n - k % n)
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head
    

        