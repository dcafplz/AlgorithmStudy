import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> hashSet = new HashSet<>();
        for (int v : nums) {
            hashSet.add(v);
        }
        return Math.min(nums.length/2,hashSet.size());
    }
}