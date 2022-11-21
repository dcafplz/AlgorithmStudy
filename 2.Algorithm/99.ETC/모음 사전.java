import java.util.Map;
import java.util.HashMap;


class Solution {
    public int solution(String word) {
        Map<Character, Integer> map = Map.of(
            'A', 0,
            'E', 1,
            'I', 2,
            'O', 3,
            'U', 4);
        int i = 781;
        int answer = 0;
        for (int j = 0; j < word.length(); j++){
            answer += map.get(word.charAt(j))*i + 1;
            i = (i-1)/5;
        }
        return answer;
    }
}