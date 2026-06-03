# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time: O(k * n)
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        res = lists[0]
        for i in range(1, len(lists)):
            res = self.merge2Lists(res, lists[i])
        
        return res

    def merge2Lists(self, list1, list2):
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

