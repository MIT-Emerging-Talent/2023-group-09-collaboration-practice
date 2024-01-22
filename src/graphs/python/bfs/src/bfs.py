from collections import deque

def bfs(graph, start, target):
    if start not in graph._adj_dict or target not in graph._adj_dict:
        return float("inf")

    visited = set()
    queue = deque([(start, 0)])

    while queue:
        current, distance = queue.popleft()
        if current == target:
            return distance

        if current not in visited:
            visited.add(current)
            neighbors = graph._adj_dict[current]
            for neighbor in neighbors:
                if neighbor.destination not in visited:
                    queue.append((neighbor.destination, distance + neighbor.distance))

    return float("inf")
