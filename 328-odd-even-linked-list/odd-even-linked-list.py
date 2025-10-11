class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        cur_node = head
        even_list = ListNode()
        tail = even_list
        while cur_node.next:
            ## move cur_node.next to even_list
            moveToTheEnd(tail, cur_node, cur_node.next)
            tail = tail.next
            if cur_node.next:
                cur_node = cur_node.next
        cur_node.next = even_list.next
        return head

def moveToTheEnd(tail, prev_node, target_node):
    if target_node == tail:
        return
    prev_node.next = prev_node.next.next
    tail.next = target_node
    target_node.next = None