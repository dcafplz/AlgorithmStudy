class Solution {
    public int solution(int n) {
        int answer = 1;
        for (int i = 1; i < n/2+1; i++){
            int k = 0;
            int j = 0;
            while (k < n){
                k += (i+j);
                j += 1;
                if (k == n){
                    answer++ ;
                    break;
                }
            }
        }
        return answer;
    }
}