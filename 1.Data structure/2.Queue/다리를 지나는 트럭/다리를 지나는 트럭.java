import java.util.LinkedList; 
import java.util.Queue; 

class Solution {
    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = bridge_length;
        Queue<Integer> bridge = new LinkedList<>();
        bridge.add(truck_weights[0]);
        int sumBridge =  truck_weights[0];
        int i = 1;
        while (i < truck_weights.length){
            time++;
            if (bridge_length <= bridge.size()){
                sumBridge -= bridge.poll();
            }
            if (weight >= sumBridge + truck_weights[i]){
                bridge.add(truck_weights[i]);
                sumBridge += truck_weights[i];
                i++;
                if (i >= truck_weights.length){
                    break;
                }
            }else{
                bridge.add(0);
            }
        }
        return time+1;
    }
}