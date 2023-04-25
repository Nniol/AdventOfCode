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

LEFT = Coord(-1,0,1)
RIGHT = Coord(1,0,1)
UP = Coord(0,-1,1)
DOWN = Coord(0,1,1)
DIRECTIONS = [(LEFT,'>'),(RIGHT,'>'),(UP,'^'),(DOWN,'v')]

def can_visit(node:Coord,offset:tuple):
    test_node = Coord(node.x+offset[0].x,node.y + offset[0].y,1,offset[1])
    if test_node.x >= 0 and test_node.x < GRID_WIDTH and \
        test_node.y >= 0 and test_node.y <= GRID_HEIGHT and \
        node.height - ord(GRID[test_node.y][test_node.x]) >= -1: # current height, can go one step up hence -1, if it is lower it will be +ve
            return True

    return False

def get_nodes_to_visit(node:Coord) -> list[Coord]:
    nodes_to_visit:list[Coord] = []
    for dir in DIRECTIONS:
        nodes_to_visit.append(can_visit(node,dir))

    return nodes_to_visit


y=0
cur_node:Coord = None
end_node:Coord = None

for line in lines:
    line = strip_line(line)
    x = 0
    for chr in line:
        if chr == 'S':
            cur_node = Coord(x=x,y=y,height=ord('a')-1,dist=0,replacement_char='S')
            GRID[y][x] =0
        elif chr == chr.upper():
            end_node = Coord(x,y,ord(chr.lower()))
            GRID[y][x] = chr.lower()
        else:
            GRID[y][x] = chr
        x+=1
    y+=1

# Build Graph
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        a_node = Coord(x=x,y=y, height=ord(GRID[y][x]),1)
        a_node.add_next_node(get_nodes_to_visit(a_node))
