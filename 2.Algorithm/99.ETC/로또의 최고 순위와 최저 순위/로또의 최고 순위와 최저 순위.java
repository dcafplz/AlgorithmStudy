class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int hit = 0, zero = 0;
        
        for(int i : lottos) {
            if(i == 0) {
                zero++;
                continue;
            }
            for(int j : win_nums) {
                if(i == j) hit++;
            }
        }
        
        return new int[] {Math.min(6,7-hit-zero),Math.min(6,7-hit)};
    }
}