import java.util.*;

class Solution {
    
    public ArrayList<int[]> hanoi(int n, int start, int to, int other, ArrayList<int[]> answer){

        if (n == 1){
            answer.add(new int[] {start, to});
        }else{
            hanoi(n-1, start, other, to, answer);
            answer.add(new int[] {start, to});
            hanoi(n-1, other, to, start, answer);
        }
        
        return answer;
    }
    
    public ArrayList<int[]> solution(int n) {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        return hanoi(n, 1, 3, 2, answer);
    }
}