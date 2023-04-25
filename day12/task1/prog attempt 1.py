import sys
import numpy as np
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line
from structs import Coord
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

lines = get_lines_from_file(day_number=12)
GRID_WIDTH = len(lines[0])-1
GRID_HEIGHT = len(lines)
GRID = np.full((GRID_HEIGHT,GRID_WIDTH),'.')
UNVISITED_NODES:list[Coord]=[]
VISITED_NODES:dict[str: Coord]={}


def is_same_point(coord1:Coord,coord2:Coord)->bool:
    return coord1.x == coord2.x and coord1.y == coord2.y

def can_visit(node:Coord):
    if node.x < 0 or node.x >= GRID_WIDTH:
        return False
    if node.y < 0 or node.y >= GRID_HEIGHT:
        return False
    node_key = node.get_node_key()
    if node.x ==5 and node.y==2:
        print (abs(node.height - ord(GRID[node.y][node.x])))
        print (node_key not in VISITED_NODES)
    if node_key not in VISITED_NODES or  node.dist < VISITED_NODES[node_key].dist:       
        if abs(node.height - ord(GRID[node.y][node.x]))>=0:
            if node.x ==5 and node.y==2:
                print (node.height,ord(GRID[node.y][node.x]))
            node.height=ord(GRID[node.y][node.x])
            return True
    return False
    

def get_nodes_to_visit(node:Coord,cur_distance: int):
    left = Coord(node.x-1,node.y,node.height,cur_distance+1,'<')
    right = Coord(node.x+1,node.y,node.height,cur_distance+1,'>')
    up = Coord(node.x,node.y-1,node.height,cur_distance+1,'^')
    down = Coord(node.x,node.y+1,node.height,cur_distance+1,'v')
    # print (node,GRID[node.y][node.x])
    nodes_to_visit:list[Coord] = []
    if can_visit(left):
        nodes_to_visit.append(left)
    if can_visit(right):
        nodes_to_visit.append(right)
    if can_visit(up):
        nodes_to_visit.append(up)
    if can_visit(down):
        nodes_to_visit.append(down)

    return nodes_to_visit



y=0
cur_node:Coord = None
end_node:Coord = None
for line in lines:
    line = strip_line(line)
    x = 0
    for chr in line:
        if chr == 'S':
            UNVISITED_NODES.append(Coord(x=x,y=y,height=ord('a')-1,dist=0,replacement_char='S'))
            GRID[y][x] =0
        elif chr == chr.upper():
            end_node = Coord(x,y,ord(chr.lower()))
            GRID[y][x] = chr.lower()
        else:
            GRID[y][x] = chr
        x+=1
    y+=1

# Build Directed Graph
graph = csr_matrix()

dijkstra(graph,indices=,return_predecessors=True)

# print (GRID)
# print ("VISITED_NODES",VISITED_NODES)
# print ("UNVISITED_NODES",UNVISITED_NODES)
cur_distance = 0
while len(UNVISITED_NODES)> 0:
    UNVISITED_NODES = sorted(UNVISITED_NODES, key=lambda x:x.dist)
    cur_node = UNVISITED_NODES.pop(0) # Ge top node
    can_visit_list = get_nodes_to_visit(cur_node,cur_distance)
    # print ("can_visit_list",can_visit_list)
    cur_node.dist = cur_distance
    GRID[cur_node.y][cur_node.x] = cur_node.replacement_char
    VISITED_NODES.update({cur_node.get_node_key(): cur_node})
    UNVISITED_NODES.extend(can_visit_list)
    cur_distance += 1
    # print ("VISITED_NODES",VISITED_NODES)
    # print ("UNVISITED_NODES",UNVISITED_NODES)
    # print (GRID)

print (VISITED_NODES[end_node.get_node_key()])


function Dijkstra(Graph, source):
 2      
 3      for each vertex v in Graph.Vertices:
 4          dist[v] ← INFINITY
 5          prev[v] ← UNDEFINED
 6          add v to Q
 7      dist[source] ← 0
 8      
 9      while Q is not empty:
10          u ← vertex in Q with min dist[u]
11          remove u from Q
12          
13          for each neighbor v of u still in Q:
14              alt ← dist[u] + Graph.Edges(u, v)
15              if alt < dist[v]:
16                  dist[v] ← alt
17                  prev[v] ← u
18
19      return dist[], prev[]