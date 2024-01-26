import heapq

def dijkstra(graph, start, target):
    if start not in graph._adj_dict or target not in graph._adj_dict:
        return float("inf")

    heap = [(0, start)]
    visited = set()

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex == target:
            return current_distance

        if current_vertex not in visited:
            visited.add(current_vertex)
            neighbors = graph._adj_dict[current_vertex]

            for neighbor in neighbors:
                neighbor_vertex, neighbor_distance = neighbor.destination, neighbor.distance
                total_distance = current_distance + neighbor_distance

                heapq.heappush(heap, (total_distance, neighbor_vertex))

    return float("inf")
