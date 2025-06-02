import java.util.*;


class Solution {
    private static List<String> res;
    private static List<String> stack;

    public List<String> generateParenthesis(int n) {
        res = new ArrayList<>();
        stack = new ArrayList<>();

        backtrack(n, 0, 0);

        return res;
    }

    private static void backtrack(int n, int openN, int closeN) {
        if (openN == closeN && closeN == n) {
            res.add(String.join("", stack));
            return;
        }

        if (openN < n) {
            stack.add("(");
            backtrack(n, openN + 1, closeN);
            stack.remove(stack.size() - 1);
        }

        if (closeN < openN) {
            stack.add(")");
            backtrack(n, openN, closeN + 1);
            stack.remove(stack.size() - 1);
        }
    }
}