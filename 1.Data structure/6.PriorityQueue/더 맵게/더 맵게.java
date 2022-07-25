import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
		PriorityQueue<Integer> h = new PriorityQueue<>();
		int answer = 0;
		
		for(int i : scoville) {
			h.add(i);
		}
		
        while (h.size() >= 2 && h.peek() < K ) {
        	h.add(h.poll() + h.poll() * 2);
        	answer += 1;
        }
		return (h.peek() >= K ? answer: -1);
    }
}