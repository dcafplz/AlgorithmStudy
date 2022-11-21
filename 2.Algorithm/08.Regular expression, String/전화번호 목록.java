import java.util.HashMap;

class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String,Integer> map = new HashMap<>();
        for(String i : phone_book){
            map.put(i,1);
        }
        for(String key : map.keySet()){
            String temp = "";
            for(int i = 0; i < key.length(); i++){
                temp += key.charAt(i);
                if (map.containsKey(temp) && !temp.equals(key)){
                    System.out.println(key);
                    return false;
                }
            }
        }
        return true;
    }   
}
