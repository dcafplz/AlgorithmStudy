import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		System.out.println(fac(n));
	}
	
	private static long fac(Long n) {
		if (n == 0 || n == 1) {
			return 1;
		}else
			return n * fac(n-1);
	}
}