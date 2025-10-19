# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        interval = 1
        amount = len(lists)
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2
        
        return lists[0]
        
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return head.next