def solution(n, wires):
    answer = 100
    for wire in wires:
        new = wires[::]
        new.remove(wire)

        visited = [wire[0]]
        to_visit = [wire[0]]
        while to_visit:
            now = to_visit.pop(0)
            for w in new:
                if w[0] == now:
                    if w[1] not in visited:
                        visited.append(w[1])
                        to_visit.append(w[1])
                elif w[1] == now:
                    if w[0] not in visited:
                        visited.append(w[0])
                        to_visit.append(w[0])
        a = len(visited)

        visited = [wire[1]]
        to_visit = [wire[1]]
        while to_visit:
            now = to_visit.pop(0)
            for w in new:
                if w[0] == now:
                    if w[1] not in visited:
                        visited.append(w[1])
                        to_visit.append(w[1])
                elif w[1] == now:
                    if w[0] not in visited:
                        visited.append(w[0])
                        to_visit.append(w[0])
        b = len(visited)
        if answer > abs(a - b):
            answer = abs(a - b)

    return answer