class Solution {
    public int solution(int n) {
        int fi1 = 0;
        int fi2 = 1;
        int temp;
        for (long i = 2; i <= n; i++){
            temp = fi1;
            fi1 = fi2;
            fi2 = (fi2+temp)%1234567;
        }
        return fi2%1234567;
    }
}