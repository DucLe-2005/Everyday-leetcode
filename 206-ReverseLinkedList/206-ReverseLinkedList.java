import java.util.LinkedList;

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode prev = null;
        while (current != null) {
            ListNode next_node = current.next;
            current.next = prev;
            prev = current;
            current = next_node;
        }
        return prev;
    }
}