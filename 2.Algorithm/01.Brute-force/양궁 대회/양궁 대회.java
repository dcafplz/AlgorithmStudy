import java.util.ArrayList;

class Solution {
    
    static ArrayList<int[]> com = new ArrayList<int[]>();
    
    public int[] solution(int n, int[] info) {
        int[] answer = {-1};
        int[] score = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
        int max_score = 0;
        combination(score, new int[n], 0, 0, n);
        for(int[] c: com){
            int[] rInfo = new int[11];
            for(int i: c){
                rInfo[i] += 1;
            }
            int a_score = 0;
            int r_score = 0;
            for(int i = 0; i < 11; i++){
                if (rInfo[i] > info[i]){
                    r_score += score[i];
                }else{
                    a_score += score[i];
                }
            }
            if (max_score < (r_score - a_score)){
                System.out.println(max_score);
                max_score = r_score - a_score;
                answer = rInfo.clone();
            }
        }
        
        return answer;
    }
    
    public static void combination(int[] arr, int[] out, int start, int depth, int r){
        if(depth == r){
            com.add(out);
            return;
        }
        for(int i=start; i<arr.length; i++){
            out[depth] = arr[i];
            combination(arr, out, i, depth+1, r);
        }
    }
}