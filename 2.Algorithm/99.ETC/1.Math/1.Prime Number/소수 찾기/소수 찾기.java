class Solution {
    public int solution(int n) {
        int answer = n-1;
        for(int i = 2; i <= n; i++){
            for(int j = 2; j < (int)Math.sqrt(i)+1; j++){
                if (i % j == 0){
                    answer -= 1;
                    break;
                }
            }
        }
        return answer;
    }
}