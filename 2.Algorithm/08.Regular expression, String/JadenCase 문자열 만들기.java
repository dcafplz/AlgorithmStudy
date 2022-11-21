class Solution {
    public String solution(String s) {
        s = s.toLowerCase();
        char[] c = s.toCharArray();
        for(int i = 0; i < c.length; i++){
            if (i == 0 || c[i-1] == ' '){
                c[i] = Character.toUpperCase(c[i]);
            }
        }
        return String.valueOf(c);
    }
}