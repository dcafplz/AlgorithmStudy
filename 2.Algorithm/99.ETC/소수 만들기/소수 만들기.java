import java.util.ArrayList;

class Solution {
    public int solution(int[] nums) {
        int count = 0;
        for(int i = 0; i < nums.length-2; i++){
            for(int j = i+1; j < nums.length-1; j++){
                for(int k = j+1; k < nums.length; k++){
                    count += isPrime(nums[i] + nums[j] + nums[k]);
                }
            }
        }
        return count;
    }

    private static int isPrime(int n) {
        if (n < 2) {return 0;}
        for(int j = 2; j < (int)Math.sqrt(n)+1; j++){
            if (n % j == 0){
                return 0;
            }
        }
        return 1;
    }
}
