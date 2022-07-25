import java.io.IOException;
import java.util.Scanner;



public class Main {

	static int count = 0;
	
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		boolean visited[] = new boolean[n + 1];
		int[][] nord = new int[n+1][n+1];

		for(int i = 0; i < m; i++) {
			int v1 = sc.nextInt();
			int v2 = sc.nextInt();
			nord[v1][v2] = 1;
			nord[v2][v1] = 1;
		}
		dfs_list(1, nord, visited);
		System.out.println(count-1);

	}

	private static void dfs_list(int v, int[][] nord, boolean[] visited) {
		visited[v] = true;
		count++;
		for(int i = 1; i <= nord.length-1; i++) {
			if(nord[v][i] == 1 && !visited[i]) {
				dfs_list(i, nord, visited);
			}
		}
	}

}