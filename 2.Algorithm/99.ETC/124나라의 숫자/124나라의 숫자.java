class Solution {
    public String solution(int n) {
        String[] num = {"1", "2", "4"};
        String answer = "";
        while (n > 0){
            n--;
            answer = num[n % 3] + answer;
            n /= 3;
        }
        return answer;
    }
}