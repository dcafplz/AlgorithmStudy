import java.io.IOException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		int v = sc.nextInt();

		boolean visited[] = new boolean[n + 1];
		int[][] nord = new int[n+1][n+1];

		for(int i = 0; i < m; i++) {
			int v1 = sc.nextInt();
			int v2 = sc.nextInt();
			nord[v1][v2] = 1;
			nord[v2][v1] = 1;
		}

		dfs(v, nord, visited);
		System.out.println("");
		Arrays.fill(visited,false);
		bfs(v, nord, visited);
		
	}

	private static void dfs(int v, int[][] nord, boolean[] visited) {
		visited[v] = true;
		System.out.print(v + " ");

		for(int i = 1; i <= nord.length-1; i++) {
			if(nord[v][i] == 1 && !visited[i]) {
				dfs(i, nord, visited);
			}
		}
	}
	
		
	public static void bfs(int v, int[][] nord, boolean[] visited) {
		Queue<Integer> q = new LinkedList<>();
		int n = nord.length - 1;

		q.add(v);
		visited[v] = true;

		while (!q.isEmpty()) {
			v = q.poll();
			System.out.print(v + " ");

			for (int i = 1; i <= n; i++) {
				if (nord[v][i] == 1 && !visited[i]) {
					q.add(i);
					visited[i] = true;
				}
			}
		}
	}
}