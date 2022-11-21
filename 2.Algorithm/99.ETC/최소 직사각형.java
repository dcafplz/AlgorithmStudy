import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int[] answer1 = new int[sizes.length];
        int[] answer2 = new int[sizes.length];
        for(int i = 0; i < sizes.length; i++){
            answer1[i] = Math.max(sizes[i][0],sizes[i][1]);
            answer2[i] = Math.min(sizes[i][0],sizes[i][1]);
        }
        return Arrays.stream(answer1).max().getAsInt() * Arrays.stream(answer2).max().getAsInt();
    }
}