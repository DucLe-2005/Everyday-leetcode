class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res  = new int[temperatures.length];
        Stack<int[]> stack = new Stack<>(); // pair: [temp, index]

        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[i] > stack.peek()[0]) {
                int[] top = stack.pop();
                int stackI = top[1];
                res[stackI] = i - stackI;
            }
            stack.push(new int[]{temperatures[i], i});
        }

        return res;
    }
}