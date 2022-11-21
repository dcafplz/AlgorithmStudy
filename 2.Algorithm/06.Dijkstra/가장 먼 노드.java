import java.util.LinkedList; 
import java.util.Queue;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(int n, int[][] edge) {
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        int[] distance = new int[n+1];
        distance[1] = 1;
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++){
            graph[i] = new ArrayList<Integer>();
        }
        
        for (int[] i : edge){
            graph[i[0]].add(i[1]);
            graph[i[1]].add(i[0]);
        }

        while(q.isEmpty() == false){
            int i = q.poll();
            for (Integer list : graph[i]){
                if (distance[list] == 0){
                    q.add(list);
                    distance[list] = distance[i] + 1;
                }
            }
        }
        return (int)(Arrays.stream(distance).filter(x -> x == Arrays.stream(distance).max().getAsInt()).count());
    }
}