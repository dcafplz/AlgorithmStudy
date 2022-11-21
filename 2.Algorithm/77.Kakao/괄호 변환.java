class Solution {
    public String solution(String p) {
        return ss(p);
    }
    
    public String ss(String p){
        int answer = 0;
        for(int i = 0; i < p.length(); i++){
            if (p.substring(i,i+1).equals("(")){
                answer += 1;
                if (answer == 0){
                    return ss("(" + ss(p.substring(i+1)) + ")" + p.substring(1,i).replaceAll("\\(","k").replaceAll("\\)","\\(").replaceAll("k","\\)"));
                }
            }else{
                answer -= 1;
                if (answer == 0){
                    return p.substring(0,i+1) + ss(p.substring(i+1));
                }
            }
        }
        return "";
    }
}