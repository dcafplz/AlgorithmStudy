def solution(bridge_length, weight, truck_weights):
    bridge = [0 for x in range(bridge_length)]
    time = bridge_length
    while len(truck_weights) > 0:
        time += 1
        bridge.pop(0)
        if weight >= sum(bridge) + truck_weights[0]:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            bridge.append(0)
    return time