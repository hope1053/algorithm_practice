def solution(bridge_length, weight, truck_weights):
    num_truck = len(truck_weights)
    sec = 0
    process, done = list(), list()
    while len(done) != num_truck:
        if len(process) != 0:
            for idx, value in enumerate(process):
                value[1] += 1
            for idx, value in enumerate(process):
                if value[1] > bridge_length:
                    done.append(value)
                    del process[idx]
        sec += 1
        if len(truck_weights) != 0:
            weight_bridge = 0
            for item in process:
                weight_bridge += item[0]
            if weight_bridge + truck_weights[0] <= weight:
                process.append([truck_weights[0],1])
                del truck_weights[0]
    return sec