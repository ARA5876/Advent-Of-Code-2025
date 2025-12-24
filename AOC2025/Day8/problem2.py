import sys 
import os
import math
sys.path.append(os.path.abspath(r"C:\Users\rajes\OneDrive\Desktop\AdventOfCode"))
import input_parser 
import operator
from collections import defaultdict
file= r'C:\Users\rajes\OneDrive\Desktop\AdventOfCode\AOC2025\Day8\input.txt'


def get_distance(i, j, coordinates):
    if i == j:
        return float('inf')
    x1, y1, z1 = coordinates[i]
    x2, y2, z2 = coordinates[j]
    return math.dist([x1, y1, z1], [x2, y2, z2])


def check_all_connected(connections, total_nodes):
    visited = set()
    queue = [0] 
    visited.add(0)

    while queue:
        node = queue.pop()
        for nbr in connections[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)

        if len(visited) == total_nodes:
            return True

    return False


lines = input_parser.get_input_as_lines(file)
coordinates = [list(map(int, line.split(","))) for line in lines]
n = len(coordinates)

distances = []
for i in range(n):
    for j in range(i + 1, n):
        dist = get_distance(i, j, coordinates)
        distances.append((dist, i, j))

distances.sort(key=lambda x: x[0])

connections = defaultdict(set)

for dist, a, b in distances:
    connections[a].add(b)
    connections[b].add(a)

    if check_all_connected(connections, n):
        print(coordinates[a][0] * coordinates[b][0])
        break

