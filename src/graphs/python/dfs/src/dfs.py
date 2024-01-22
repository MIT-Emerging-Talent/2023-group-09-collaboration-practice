# iterative dfs

def dfs(graph, start, target):
    if start not in graph._adj_dict or target not in graph._adj_dict:
        return float("inf")

    visited = set()
    stack = [(start, 0)]

    while stack:
        current, distance = stack.pop()

        if current == target:
            return distance

        if current not in visited:
            visited.add(current)
            neighbors = graph._adj_dict[current]

            for neighbor in reversed(neighbors):
                if neighbor.destination not in visited:
                    stack.append((neighbor.destination, distance + neighbor.distance))

    return float("inf")

