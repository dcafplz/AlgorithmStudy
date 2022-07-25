import java.util.Arrays;

class Solution {
    public int[] solution(int n, String[] words) {
        boolean first = false;
        for (int i = 1; i < words.length; i++){
            String s = words[i];
            if (Arrays.stream(words).filter(x -> x.equals(s)).count() >= 2){
                if(first || i == words.length-1){
                    return new int[] {i % n + 1, i / n + 1};
                }else{
                    first = true;
                }
            }else if(words[i-1].charAt(words[i-1].length()-1) != words[i].charAt(0)){
                return new int[] {i % n + 1, i / n + 1};
            }
        }
        return new int[] {0, 0};
    }
}