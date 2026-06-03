# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # space: O(1)
        # time: O(log(k) * n)


        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        while len(lists) != 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    new_lists.append(lists[i])
                    break
                new_lists.append(self.merge2Lists(lists[i], lists[i+1]))
            lists = new_lists
        
        return lists[0]

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

