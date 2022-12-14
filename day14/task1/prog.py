from collections import namedtuple
import sys
import numpy as np
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line
from structs import Coord
lines = get_lines_from_file(day_number=14)

CAVERN = np.full((1000,200),' ')

class NoWhereToGoException(Exception):
    pass

def get_coord(coord_as_str:str)->Coord:
    coord = coord_as_str.split(',')
    return Coord(x = int(coord[0]),y=int(coord[1]))

def get_offset(start:Coord,end:Coord):
    if (start.x == end.x):
        if start.y < end.y:
            return Coord(x=0,y=1)
        return Coord(x=0,y=-1)
    if (start.y == end.y):
        if start.x < end.x:
            return Coord(x=1,y=0)
        return Coord(x=-1,y=0)

def get_grain_offset(grain:Coord) -> Coord:
    if CAVERN[grain.x][grain.y+1]==' ':
        return Coord(0,+1)
    if CAVERN[grain.x-1][grain.y+1]==' ':
        return Coord(-1,+1)
    if CAVERN[grain.x+1][grain.y+1]==' ':
        return Coord(1,+1)
    raise NoWhereToGoException
        
def is_same_point(coord1:Coord,coord2:Coord)->bool:
    return coord1.x == coord2.x and coord1.y == coord2.y



# Build cavern
for line in lines:
    line = strip_line(line)
    line = line.replace(' ','')
    coords:list = line.split('->') # Draw it backward
    coords.reverse()
    st_coord:Coord = None
    ed_coord:Coord = None
    for coord in coords:
        st_coord = get_coord(coord)
        if ed_coord is not None:
            # do stuff
            offset = get_offset(st_coord,ed_coord)
            traversal_coord:Coord =st_coord.copy()
            while not is_same_point(traversal_coord,ed_coord):
                CAVERN[traversal_coord.x][traversal_coord.y]='#'
                traversal_coord.x += offset.x
                traversal_coord.y += offset.y
            CAVERN[ed_coord.x][ed_coord.y]='#'
        ed_coord = st_coord
view_start = Coord(494,0)
view_end = Coord(503,9)

# out_str = ""
# y = view_start.y
# while y <= view_end.y:
#     x=view_start.x
#     while x <= view_end.x:
#         out_str += CAVERN[x][y]
#         x+=1
#     out_str+="\r\n"
#     y+=1
# print (out_str)

SAND_START:Coord = Coord(500,0)
sand_grain_count:int = 0
try:
    while True:
        grain = SAND_START.copy()
        try:
            while True:
                offset = get_grain_offset(grain)
                grain.x += offset.x
                grain.y += offset.y
        except NoWhereToGoException:
            CAVERN[grain.x][grain.y]='o'
            sand_grain_count+=1
        # if sand_grain_count == 25:
        #      raise IndexError()
except IndexError:
    print (sand_grain_count)

# out_str = ""
# y = view_start.y
# while y <= view_end.y:
#     x=view_start.x
#     while x <= view_end.x:
#         out_str += CAVERN[x][y]
#         x+=1
#     out_str+="\r\n"
#     y+=1
# print (out_str)

    
