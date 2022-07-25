class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        for(int i = (n > m ? m : n); i > 0; i--){
            if (m % i == 0 && n % i == 0){
                answer[0] = i;
                answer[1] = n*m/i;
                return answer;
            } 
        }
        return null;
    }
}