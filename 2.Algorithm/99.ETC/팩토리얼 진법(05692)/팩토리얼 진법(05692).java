import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> n = new ArrayList<>();
		while(true) {
			int temp = sc.nextInt();
			if (temp == 0) {
				break;
			}else {
				n.add(temp);
			}	
		}
		for(int i: n) {
			System.out.println(factorialNotion(i));
		}
	}

	private static int factorialNotion(int n) {
		int fac = 1;
		int i = 1;
		int answer = 0;
		while (n >= 1) {
			int m = n % 10;
			n /= 10;
			answer += m * fac;
			fac *= (++i);
		}
		return answer;
	}

}