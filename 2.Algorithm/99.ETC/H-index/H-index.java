import java.util.Arrays;

class Solution {
    public long solution(int[] citations) {
        int max = Arrays.stream(citations).max().getAsInt();
        for (int i = max; i > -1; i--){
            int hindex = 0;
            for (int j: citations){
                if (j >= i){hindex++;}
            }
            if (hindex >= i){
                return Math.min(hindex, i);
            }
        }
        return 0;
    }
}