import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		String s = "";
		System.out.println(binary(n, s));
	}

	private static String binary(long n, String s) {
		if(n == 0) {
			return s;
		}else {
			return binary(n/2, (n%2)+s);
		}
	}

}