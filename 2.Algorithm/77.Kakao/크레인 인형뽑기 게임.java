import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();
        int answer = 0;
        for (int i : moves){
            int k = 0;
            while (board[k][i-1] == 0 && k < board.length-1){
                k += 1;
            }
            if (!stack.empty() && stack.peek() == board[k][i-1]){
                stack.pop();
                answer += 2;
            }else if (board[k][i-1] != 0){
                stack.push(board[k][i-1]);
            }
            board[k][i-1] = 0;
        }
        return answer;
    }
}