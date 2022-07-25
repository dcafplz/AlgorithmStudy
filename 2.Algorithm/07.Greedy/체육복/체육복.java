import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Arrays.sort(lost);
        Arrays.sort(reserve);
        int answer = n-lost.length;
        for(int i = 0; i < reserve.length; i++){
            if (Arrays.binarySearch(lost, reserve[i]) >= 0){
                lost[Arrays.binarySearch(lost, reserve[i])] = -1;
                answer += 1;
            }else if(Arrays.binarySearch(lost, reserve[i]-1) >= 0){
                lost[Arrays.binarySearch(lost, reserve[i]-1)] = -1;
                answer += 1;
            }else if(Arrays.binarySearch(lost, reserve[i]+1) >= 0 && !(Arrays.binarySearch(reserve, reserve[i]+1) >= 0)){
                lost[Arrays.binarySearch(lost, reserve[i]+1)] = -1;
                answer += 1;
            }
        }
        return answer;
    }
}