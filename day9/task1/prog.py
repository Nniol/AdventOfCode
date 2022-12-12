import sys
import numpy as np

sys.path.append('..\..')
sys.path.append('..')

from structs import Offset,KnotPos
from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=9)

GRID_SIZE = 1000

# Setup
hk = KnotPos(500,500)
tk = KnotPos(500,500)
offset = Offset(row = 0,col=0)
grid = np.full((GRID_SIZE,GRID_SIZE),False)
grid[tk.row,tk.col]=True

COMMAND_DOWN = 'D'
COMMAND_UP = 'U'
COMMAND_LEFT = 'L'
COMMAND_RIGHT = 'R'

def get_tail_offset(hk:KnotPos,tk:KnotPos)->Offset:
    col_dir_mod = 1
    row_dir_mod = 1
    if hk.col - tk.col<0:
        col_dir_mod=-1
    if hk.row - tk.row<0:
        row_dir_mod=-1
    distance= abs(hk.row-tk.row)+abs(hk.col-tk.col)
    # print (distance)

    if distance == 1 or (hk.row == tk.row and hk.col == tk.col):
        return Offset(row = 0,col =0)
    if hk.row == tk.row:
        return Offset(row = 0,col =1 * col_dir_mod)
    if hk.col == tk.col:
        return Offset(row = 1 * row_dir_mod,col =0)
    # Now check diagonal touch
    if distance == 2: # Diagonal touch
        return Offset(row = 0,col =0)
    return Offset(row = 1 * row_dir_mod,col = 1 * col_dir_mod)


for line in lines:
    line = strip_line(line)
    command = line.split(' ')
    # print ("command",command)
    count = int(command[1])
    if command[0]==COMMAND_DOWN:
        offset=Offset(row=1,col=0)
    elif command[0]==COMMAND_UP:
        offset=Offset(row=-1,col=0)
    elif command[0]==COMMAND_RIGHT:
        offset=Offset(row=0,col=1)
    elif command[0]==COMMAND_LEFT:
        offset=Offset(row=0,col=-1)
    # print ("offset",offset)
    for i in range(count):
        hk.move(offset)
        tail_offset = get_tail_offset(hk,tk)
        # print ("tail_offset",tail_offset)
        tk.move(tail_offset)
        print (tk)
        grid[tk.row,tk.col]=True
        # knot_pos = np.full((GRID_SIZE,GRID_SIZE),'.')
        # knot_pos[hk.row,hk.col] = 'H'
        # knot_pos[tk.row,tk.col] = 'T'
        # print (knot_pos)


print (np.count_nonzero(grid))
