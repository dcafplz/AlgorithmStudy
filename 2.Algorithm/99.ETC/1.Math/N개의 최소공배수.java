import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {
        Arrays.sort(arr);
        int answer = 1;
        for (int i : arr){
            for (int j = i; j > 0; j--){
                if (answer % j == 0 && i % j == 0){
                    answer = i * answer / j;
                    break;
                }
            }
        }
        return answer;
    }
}