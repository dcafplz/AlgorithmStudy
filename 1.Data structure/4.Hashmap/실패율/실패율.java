import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> solution(int N, int[] stages) {
        
		HashMap<Integer, Double> counts = new HashMap<>();

		for (int i : stages) {
			if (counts.containsKey(i)) {
				counts.put(i, counts.get(i) + 1);
			} else
				counts.put(i, (double) 1);
		}


		int stage = stages.length;

		for (int i = 1; i <= N; i++) {
			if (counts.containsKey(i)) {
				stage -= counts.get(i);
				counts.put(i, (double) counts.get(i) / (double) (stage + counts.get(i)));
			} else {
				counts.put(i, (double) 0);
			}
		}
		counts.remove(N + 1);

		List<Double> d = counts.values().stream().collect(Collectors.toList());

		return counts.keySet().stream().sorted(Comparator.comparing(counts::get).reversed()).collect(Collectors.toList());

    }
}