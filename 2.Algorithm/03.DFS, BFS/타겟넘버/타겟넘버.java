class Solution {

    public int solution(int[] numbers, int target) {
        int answer = 0;
        answer = re(numbers, target, 0, 0);
        return answer;
    }

    int re(int[] numbers, int target, int sum, int n){
        if(numbers.length == n){
            if(sum == target){
                return 1;
            }
            return 0;
        }
        return re(numbers, target, sum + numbers[n], n + 1) + re(numbers, target, sum - numbers[n], n + 1); 
    }
}