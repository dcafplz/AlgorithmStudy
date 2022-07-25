import java.util.ArrayList;

class Solution {
    
    public ArrayList<Long> solution(long begin, long end) {
        ArrayList<Long> answer = new ArrayList<Long>();
        for(long i = begin; i < end+1; i++){
            answer.add(p(i));
        }
        return answer;
    }
    
    public long p(long n){
        for (long i = 2; i < Math.sqrt(n); i++){
            if (n % i == 0 && n/i <= 10000000){
                return n/i;
            }
        }
        return 1;
    }
}