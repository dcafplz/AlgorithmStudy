import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public Integer[] solution(String[] id_list, String[] report, int k) {
        Map<String, Integer> reporter = new HashMap<>();
		Map<String, Integer> reportee = new HashMap<>();
	
		
		report = Arrays.stream(report).distinct().toArray(String[]::new);
		
		for(String s: report) {
			String[] temp = s.split(" ");
			reportee.put(temp[1], reportee.getOrDefault(temp[1], 0)+1);
		}
		
		for(String s: report) {
			String[] temp = s.split(" ");
			if (reportee.getOrDefault(temp[1], -1) >= k) {
				reporter.put(temp[0], reporter.getOrDefault(temp[0], 0)+1);
			}
		}
		
		return Arrays.stream(id_list).map(i -> reporter.getOrDefault(i,0)).toArray(Integer[]::new);
    }
}