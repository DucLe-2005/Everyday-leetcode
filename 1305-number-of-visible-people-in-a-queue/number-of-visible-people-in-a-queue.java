class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int N = heights.length;
        int[] res = new int[N];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = N - 1; i >= 0; i--) {
            int height = heights[i];
            int visible = 0;

            // count all shorter person that are visible
            while (!stack.isEmpty() && height > stack.peek()) {
                visible++;
                stack.pop();
            }

            // If there's someone taller or equal, they're also visible
            if (!stack.isEmpty()) visible++;

            res[i] = visible;
            stack.push(height);
        }

        return res;
    }
}