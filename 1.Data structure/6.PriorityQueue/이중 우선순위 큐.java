import java.util.Collections;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] operations) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for(String s : operations){
            String[] temp = s.split(" ");
            if (temp[0].equals("I")){
                answer.add(Integer.parseInt(temp[1]));
            }else if(temp[0].equals("D") && answer.size() > 0){
                Collections.sort(answer);
                if (temp[1].equals("-1")){
                    answer.remove(0);
                }else
                    answer.remove(answer.size()-1);
            }
        }
        if (answer.size() > 0){
            Collections.sort(answer);
            return new int[] {answer.get(answer.size()-1),answer.get(0)};
        }else{
            return new int[] {0,0};    
        }
    }
}