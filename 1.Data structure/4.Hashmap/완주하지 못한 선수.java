import java.util.HashMap;

class Solution {
    public HashMap toHash(HashMap<String,Integer> map, String[] list){
        for(String i : list){
            if (map.containsKey(i)){
                map.put(i,map.remove(i)+1);
            }else{
                map.put(i,1);
            }
        }
        return map;
    } 
    
    public String solution(String[] participant, String[] completion) {
        HashMap<String,Integer> map = new HashMap<>();
        map = toHash(map,participant);
        map = toHash(map,completion);
        for(String key : map.keySet()){
            if (map.get(key) % 2 == 1){
                return key;
            }
        }
        return null;
    }
}