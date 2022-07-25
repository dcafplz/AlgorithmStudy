import java.util.ArrayList;

class Solution {
    public ArrayList solution(int[] answers) {
        int[] a1 = {1,2,3,4,5};
        int[] a2 = {2,1,2,3,2,4,2,5};
        int[] a3 = {3,3,1,1,2,2,4,4,5,5};
        int[] count = {0,0,0};
        for (int i = 0; i < answers.length; i++){
            count[0] += (a1[i%5] == answers[i] ? 1 : 0);
            count[1] += (a2[i%8] == answers[i] ? 1 : 0);
            count[2] += (a3[i%10] == answers[i] ? 1 : 0);
        }
        int best = Math.max(count[2],Math.max(count[0],count[1]));
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < 3; i++){
            if (count[i] == best){
                answer.add(i+1);
            }
        }
        return answer;
    }
}