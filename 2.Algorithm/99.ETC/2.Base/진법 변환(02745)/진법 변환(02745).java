import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] a = br.readLine().split(" ");
		int notion = Integer.parseInt(a[1]);
		char[] aa = a[0].toCharArray();
		long answer = 0;
		int exp = 0;
		for(int i : aa) {
			answer *= notion;
			answer += (i >= 65 ? (i-65+10) : (i-48));
			exp += 1;
		}
		System.out.println(answer);
	}
}
