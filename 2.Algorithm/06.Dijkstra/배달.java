import java.util.Arrays;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int[] answer = new int[N];
        boolean[] visited = new boolean[N];
        Arrays.fill(answer,500001);
        Arrays.fill(visited,false);
        answer[0] = 0;
        int start = 0;
        while (true){
            visited[start] = true;
            for (int[] i: road){

                if (i[0]-1 == start && visited[i[1]-1] == false){
                    answer[i[1]-1] = Math.min(answer[i[1]-1], answer[start] + i[2]);
                }else if(i[1]-1 == start && visited[i[0]-1] == false){
                    answer[i[0]-1] = Math.min(answer[i[0]-1], answer[start] + i[2]);
                }
                
            }
            int min = 500001;
            for (int i = 1; i < N; i++){
                if (visited[i] == false && min >= answer[i]){
                    start = i;
                    min = answer[i];
                }
            }
            if(min == 500001){
                break;
            }
        }
        return (int)Arrays.stream(answer).filter(x -> x <= K).count();
    }
}