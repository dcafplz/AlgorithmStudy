import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		int x = sc.nextInt();

		Queue<Integer> q = new LinkedList<>();
	    q.add(x);
	    int[] distance = new int[n+1];
	    ArrayList<Integer>[] graph = new ArrayList[n+1];
	    for (int i = 0; i < n+1; i++){
	        graph[i] = new ArrayList<Integer>();
	        distance[i] = -1; 
	    }
	    distance[x] = 0;
        for (int i = 0; i < m; i++){
            graph[sc.nextInt()].add(sc.nextInt());
        }
        
        while(!q.isEmpty()){
            int i = q.poll();
            for (Integer list : graph[i]){
                if (distance[list] == -1){
                    q.add(list);
                    distance[list] = distance[i] + 1;
                }
            }
        }
        
        boolean is = false;
        for (int i = 1 ; i <= n; i++) {
        	if (distance[i] == k && i != x) {
        		System.out.println(i);
        		is = true;
        	}
        }
        if (is == false) {System.out.println(-1);}
        
	}
}