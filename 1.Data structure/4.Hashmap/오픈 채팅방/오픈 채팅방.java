import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    public List<String> solution(String[] record) {
		        ArrayList<String[]> answer = new ArrayList<>();
		        Map<String, String> msgMap = new HashMap<String, String>();
		        Map<String, String> map = new HashMap<String, String>();
		        
		        msgMap.put("Enter","님이 들어왔습니다.");
		        msgMap.put("Leave","님이 나갔습니다.");
		        
		        for(String s : record){
		            String[] temp = s.split(" ");
		            if (!temp[0].equals("Change")){
		                answer.add(new String[] {temp[1],temp[0]});
		            }
		            if (!temp[0].equals("Leave")){
		                map.put(temp[1], temp[2]);
		            }
		        }
		        return answer.stream().map(x -> map.get(x[0]) + msgMap.get(x[1])).collect(Collectors.toList());
    }
}