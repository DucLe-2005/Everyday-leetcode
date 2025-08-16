# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKthNode(groupPrev, k)

            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr