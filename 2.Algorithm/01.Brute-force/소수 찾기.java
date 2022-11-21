import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {

    private static int isPrime(int n) {
    	if (n < 2) {return 0;}
    	for(int j = 2; j < (int)Math.sqrt(n)+1; j++){
            if (n % j == 0){
                return 0;
            }
        }
        return 1;
    }
    
	private static void permutation( String[] numbers, boolean[] isChecked, int dept, String[] result,  Set<Integer> totalList ) {
	    for ( int i = 0; i < numbers.length; i++ ) {
	        if( !isChecked[i] ) {
	            isChecked[i] = true;
	            result[dept] = numbers[i];
	            totalList.add(Integer.parseInt(String.join("", result)));
	            permutation(numbers, isChecked, dept + 1, result, totalList);
	            isChecked[i] = false; 
	            result[dept] = ""; 
	            }
	    }
	}
    
    public int solution(String number) {
		String[] numbers = number.split("");
        boolean[] isChecked = new boolean[numbers.length];
	    Set<Integer> totalList = new HashSet<Integer>();
	    String[] result = new String[numbers.length];
	    Arrays.fill(result, "");
	    permutation(numbers, isChecked, 0, result, totalList);
	    int answer = 0;
	    for (int i : totalList) {
	        answer += isPrime(i);
	    }
        return answer;
    }
}