import java.util.Map;
import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMapString, Integer map = new HashMap();
        
        for (String[] s clothes){
            map.put(s[1],map.getOrDefault(s[1],0)+1);
        }
        
        for (int i map.values()){
            answer = (i+1);
        }
        
        return answer - 1;
    }
}