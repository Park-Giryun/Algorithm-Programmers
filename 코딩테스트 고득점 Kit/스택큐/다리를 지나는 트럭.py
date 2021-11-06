from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0
    trucks_on_bridge = deque([0 for _ in range(bridge_length)])
    while trucks_on_bridge:
        answer += 1
        removed_truck = trucks_on_bridge.popleft()
        bridge_weight -= removed_truck

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)
                bridge_weight += new_truck
                trucks_on_bridge.append(new_truck)
            else:
                trucks_on_bridge.append(0)
    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))