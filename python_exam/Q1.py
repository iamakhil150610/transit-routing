"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""






def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        # Enter your code here
        return graph_object
    except:
        return graph_object


def Q1_dijkstra(G, S, T) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
	start = [Queue(S, 0.0)]                       # Creating initial start node using HeapQ and setting its value to 0.0
	    goal = set()
	    pred = dict()                                                         # Dictionary to store visited nodes in a graph
	    dist = dict()                                                     # Dictionary to store distance from point to point
	    pred[S] = None
	    dist[S] = 0.0
	    while start:
		C = hq.heappop(start).v                   # Pop the smallest item off the heap, maintaining the heap invariant.
		if C == T:
		    return traversal(T, pred)
		goal.add(C)
		for pointer in G[C]:
		    if pointer in goal:
			continue
		    dist_temp = dist[C] + G[C][pointer]['weight']
		    if pointer not in dist or dist[pointer] > dist_temp:                          #Checking vertex with low cost
			dist[pointer] = dist_temp
			pred[pointer] = C
			hq.heappush(start, Queue(pointer, dist[C] + G[C][pointer]['weight']))          # Adding vertex to queue
	    return []

    shortest_path_distance = -1
    try:
        # Enter your code here
        return shortest_path_distance
    except:
        return shortest_path_distance
