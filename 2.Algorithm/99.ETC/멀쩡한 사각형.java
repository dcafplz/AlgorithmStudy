class Solution {
    public long solution(long w, long h) {
        long answer = w * h - w - h;
        if (w < h){
            long temp = w;
            w = h;
            h = temp;
        }
        while (h != 0){
            long temp = h;
            h = w % h;
            w = temp;
        }
        return answer + w;
    }
}