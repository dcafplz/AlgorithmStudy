import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int right = people.length-1;
        int left = 0;
        while (right >= left){
            if (people[right] + people[left] <= limit){
                left += 1;
            }
            right -= 1 ;
            answer += 1;
                
        }
        return answer;
    }
}