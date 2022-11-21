import java.util.Scanner;

public class Main {
	
	static int[] a;
	static int[] dp;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		a = new int[sc.nextInt()+1];
		dp = new int[a.length];
		for(int i = 1; i < a.length; i++) {
			a[i] = sc.nextInt();
		}
		
		dp[1] = a[1];
		 
		if (a.length > 2) {
			dp[2] = a[1] + a[2];
		}
		
		System.out.println(rcur(a.length-1));

	}

	static int rcur(int i) {
		
		if (dp[i] == 0 && i > 2) {
			dp[i] = a[i] + Math.max(rcur(i-3) + a[i-1], rcur(i-2));			
		}
		
		return dp[i];
		
	}
}
