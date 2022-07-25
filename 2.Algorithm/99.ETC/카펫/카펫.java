class Solution {
    public int[] solution(int brown, int yellow) {
        for(int i = brown + yellow; i > 0; i--){
            if ((brown+yellow)%(i+2) == 0 && yellow%i == 0){
                return new int[] {i+2, (brown+yellow)/(i+2)};
            }
        }
    }
}