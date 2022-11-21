import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public ArrayList solution(int[] numbers) {
        Set<Integer> answer = new HashSet<Integer>();
        for(int i = 0; i < numbers.length-1; i++){
            for(int j = i+1; j < numbers.length; j++)
                answer.add(numbers[i] + numbers[j]);
        }
        ArrayList<Integer> list = new ArrayList<>(answer); 
        Collections.sort(list);
        return list;
    }
}