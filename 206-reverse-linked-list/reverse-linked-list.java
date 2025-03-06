import java.util.LinkedList;

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newNode = null;
        ListNode currentNode = head;

        while (currentNode != null) {
            ListNode temp = currentNode.next;
            currentNode.next = newNode;
            newNode = currentNode;
            currentNode = temp;
        }

        return newNode;
    }
}