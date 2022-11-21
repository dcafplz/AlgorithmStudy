import java.util.Arrays;

class Solution {
    public String solution(String s) {
        return Arrays.stream(s.split(" ")).map(Integer::parseInt).min(Integer::compare).get() + " " + Arrays.stream(s.split(" ")).map(Integer::parseInt).max(Integer::compare).get();
    }
}