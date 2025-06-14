class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < temperatures.length; i++) {
            int temp = temperatures[i];
            while (!stack.isEmpty() && temp > stack.peek()[0]) {
                int[] top = stack.pop();
                int index = top[1];
                res[index] = i - index;
            }
            stack.push(new int[]{temp, i});
        }        
        return res;
    }
}