import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public boolean isValid(String s) {
        char[] sArray = s.toCharArray();
        List<Character> stack = new ArrayList<>();
        HashMap<Character, Character> closeToOpen = new HashMap<>();
        closeToOpen.put(')', '(');
        closeToOpen.put('}', '{');
        closeToOpen.put(']', '[');        

        for (char c : sArray) {
            if (closeToOpen.containsKey(c)) {
                if (stack.size() != 0 && stack.get(stack.size() - 1) == closeToOpen.get(c)) {
                    stack.remove(stack.size() - 1);
                }
                else {
                    return false;
                }
            } else {
                stack.add(c);
            }
        }

        if (stack.size() != 0) {
            return false;
        }

        return true;
    }
}