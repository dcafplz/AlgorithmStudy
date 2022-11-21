import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		br.readLine();
		String s = br.readLine();
		long answer = 0;
		final long prime = 1234567891;
		long thirtyone = 1;
		for(int i = 0; i < s.length(); i++) {
			answer += (((int)s.charAt(i) - 96) * thirtyone)%prime;
			thirtyone = thirtyone * 31 % prime;
		}
		System.out.println(answer%prime);
	}
}