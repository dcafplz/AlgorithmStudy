import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];
        Stack<Integer> stack = new Stack<>();
        int i,temp;
        stack.push(0);   
        for (i = 1; i < len; i++){
            while(!stack.empty() && prices[stack.peek()] > prices[i]){
                temp = stack.pop();
                answer[temp] = i-temp;
            }
            stack.push(i);
        }
        while (!stack.empty()){
            temp = stack.pop();
            answer[temp] = len - temp-1;
        }
        
        return answer;
    }
}

// 일반 풀이
        // int len = prices.length;
        // int[] answer = new int[len];
        // int i;
        // for (i = 0; i < len-1; i++){
        //     int k = i;
        //     while (prices[i] <= prices[k]){
        //         k += 1;
        //         if (k >= len - 1){
        //             break;
        //         }
        //     }
        //     answer[i] = k-i;
        // }