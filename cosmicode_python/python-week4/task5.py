import heapq

def graph():
    adding_node = True
    diction = {}
    while adding_node:
        node1 = input("Enter 1st the node: ")
        node2 = input("Enter 2nd node: ")
        weight = int(input("Enter their weight: "))
        if node1 not in diction:
            diction[node1] = {}
        if node2 not in diction:
            diction[node2] = {}
        diction[node1][node2] = weight
        diction[node2][node1] = weight
        choose = input("want to enter more (y/n)? ")
        if choose.lower() == 'n':
            adding_node = False
    return diction

def dijkstra(graph):
    source = input("Enter the source: ")
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    visited = set()
    priority = [(0, source)]  
    
    while priority:
        distance, node = heapq.heappop(priority)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority, (new_distance, neighbor))
    
    print("\nShortest Distances from source:", source)
    for node, distance in distances.items():
        print(f"{node}: {distance}")

print("DIJKSTRA")
making = graph()
dijkstra(making)
