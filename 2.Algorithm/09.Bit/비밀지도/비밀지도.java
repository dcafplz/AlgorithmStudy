class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[arr1.length];
        String a = " ".repeat(n);
        for(int i = 0; i < arr1.length; i++){
            answer[i] = (a + Integer.toBinaryString(arr1[i] | arr2[i]).replace("0"," ").replace("1","#"));
            answer[i] = answer[i].substring((answer[i].length())-n, (answer[i].length()));
        }
        return answer;
    }
}