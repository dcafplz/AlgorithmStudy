import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        int cnt = 1;
        int[] answer = new int[speeds.length];
        int iMax = 0;
        ArrayList<Integer> integers1 = new ArrayList<Integer>();
        for(int i = 0; i< progresses.length; i++){
            for(int j : answer){
                iMax = Math.max(j,iMax);
            }
            answer[i] = (int)Math.ceil((100-(double)progresses[i])/(double)speeds[i]);
            if (i>=1 && iMax >= answer[i]){
                cnt+=1;
            }else if(i != 0){
                integers1.add(cnt);
                cnt = 1;
            }
        }

        integers1.add(cnt);
        return integers1;
    }
}