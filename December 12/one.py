from numpy import inf
import random

with open("input.txt") as f:
    contents = f.read().strip().split('\n')

def get_adjacent_squares(pos, board):
    edges = [(pos[0] - 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1), (pos[0] + 1, pos[1])]

    # only return edges on board
    height = len(board)
    width = len(board[0])

    return [edge for edge in edges if -1 < edge[0] < width and -1 < edge[1] < height]

def get_height(pos, board): 
    return heights.index(board[pos[1]][pos[0]])

# create map
heights = 'SabcdefghijklmnopqrstuvwxyzE'
height_map = [list(row) for row in contents]

# create graph from map
start = None
end = None

graph = {}
for row in range(len(height_map)):
    for col in range(len(height_map[row])):
        if height_map[row][col] == "S": start = (col, row)
        if height_map[row][col] == "E": end = (col, row)

        # get edges
        edges = get_adjacent_squares((col, row), height_map)

        # add only those that are 1 higher or less
        graph[(col, row)] = [edge for edge in edges if get_height(edge, height_map) - get_height((col, row), height_map) <= 1]


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0

    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

print(len(shortest_path(graph, start, end)) - 1)

"""
# perform djikstras algorithm from start to end
costs = {}
costs[start] = 0
for pos in graph:
    if pos != start: costs[pos] = inf

parents = {}

next_node = start

while height_map[next_node[1]][next_node[0]] != 'E':

    for neighbor in graph[next_node]:
        if neighbor not in costs: continue

        if costs[next_node] + 1 < costs[neighbor]:
            costs[neighbor] = costs[next_node]
            parents[neighbor] = next_node
        
        next_index = graph[neighbor].index(next_node)
        del graph[neighbor][next_index]

    del costs[next_node]

    next_node = min(costs, key=costs.get)

print(parents[start])
"""