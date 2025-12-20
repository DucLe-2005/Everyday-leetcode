# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        p1, p2 = None, None
        h1, h2 = None, None
        curr = head
        print("1")
        while curr:
            if curr.val < x:
                if not p1:
                    p1 = curr
                    h1 = p1
                else:
                    p1.next = curr
                    p1 = curr
            else:
                if not p2:
                    p2 = curr
                    h2 = p2
                else:
                    p2.next = curr
                    p2 = curr
            curr = curr.next
        
        # Return head if either of the parition is empty
        if not h1 or not h2:
            return head
        
        p1.next = h2
        p2.next = None
        return h1

        
        
                


        


