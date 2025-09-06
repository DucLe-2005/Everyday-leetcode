# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # if odd, move slow to next node
        if fast:
            slow = slow.next
        
        first = head
        second = self.reverse(slow)

        while first and second:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True
    
    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev

