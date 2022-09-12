class Solution {
    public int solution(String s) {
        String[] alphabets = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        for(int i = 0; i < 10; i++){
            s = s.replaceAll(alphabets[i],""+i);
        }
        return Integer.parseInt(s);
    }
}