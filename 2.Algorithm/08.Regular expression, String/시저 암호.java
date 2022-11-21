class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        char[] slist = s.toCharArray(); 
        for(int i: slist){
            if (i == 32){
                sb.append(" ");
            }else if ((i >= 97 && i+n > 122) || (i <= 90 && i >= 65 && i+n > 90)){
                sb.append((char)(i+n-26));
            }else {
                sb.append((char)(i+n));
            }
        }
        return sb.toString();
    }
}