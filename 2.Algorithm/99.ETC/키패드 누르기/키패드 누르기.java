class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[] left = {3,1};
        int[] right = {3,3};
        double handadd = (hand.equals("left") ? -0.1 : 0.1);
        for (int i : numbers){
            i = (i > 0 ? i : 11);
            if (i % 3 == 1){
                answer += "L";
                left = new int[] {i/3, 1}; 
            }else if (i % 3 == 0){
                answer += "R";
                right = new int[] {i/3-1,3};
            }else{
                double distanceLeft = Math.abs(left[0] - (i/3)) + 
                    Math.abs(left[1]-(i%3)) + handadd;
                int distanceRight = Math.abs(right[0] - (i/3)) + 
                    Math.abs(right[1]-(i%3));
                if (distanceLeft < distanceRight){
                    answer += "L";
                    left = new int[] {i/3, 2}; 
                }else {
                    answer += "R";
                    right = new int[] {i/3,2};
                }
            }
        }
        return answer;
    }
}