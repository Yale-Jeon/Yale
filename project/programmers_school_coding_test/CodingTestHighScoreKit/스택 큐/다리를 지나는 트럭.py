def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    time = 0
    while True:
        if len(truck_weights) == 0:
            time += bridge_length
            break
        bridge.pop(0)
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            n = 0
            for i in bridge:
                if i == 0:
                    time += 1
                    n += 1
                else:
                    break
            bridge = bridge[n:] + [0] * (n + 1)
        time += 1

    answer = time
    return answer