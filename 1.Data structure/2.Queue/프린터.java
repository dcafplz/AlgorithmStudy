import java.util.LinkedList;
import java.util.Queue;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Integer> q = new LinkedList<Integer>();
        Queue<Integer> p = new LinkedList<Integer>();
        for(int i = 0; i < priorities.length; i++){
            q.offer(priorities[i]);
            p.offer(i);
        }
        int max = q.stream().max(Integer::compare).orElse(-1);
        int answer = 0;
        while(!q.isEmpty()){
            int tempq = q.poll();
            int tempp = p.poll();
            if (tempq < max){
                q.offer(tempq);
                p.offer(tempp);
            }else if(tempp == location){
                return answer + 1;
            }else{
                max = q.stream().max(Integer::compare).orElse(-1);
                answer++;
            }
        }

        return 0;
    }
}