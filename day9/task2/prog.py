import sys
import numpy as np

sys.path.append('..\..')
sys.path.append('..')

from structs import Offset,KnotPos
from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=9)

GRID_SIZE = 500
NUMBER_OF_TAILS = 9
# Setup
hk = KnotPos(int(250),int(250))
tks:dict[int:KnotPos] = {}
for i in range(NUMBER_OF_TAILS):
    tks.update({i: KnotPos(int(250),int(250))})

for key,value in tks.items():
    print (f"{key}: {value}")

offset = Offset(row = 0,col=0)
grid = np.full((GRID_SIZE,GRID_SIZE),'.')
grid[tks[NUMBER_OF_TAILS-1].row,tks[NUMBER_OF_TAILS-1].col]='#'

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
        tail_offset = get_tail_offset(hk,tks[0])
        tks[0].move(tail_offset)
        index = 1
        while (index<NUMBER_OF_TAILS):
            tail_offset = get_tail_offset(tks[index-1],tks[index])
            tks[index].move(tail_offset)
            index+=1

        grid[tks[NUMBER_OF_TAILS-1].row,tks[NUMBER_OF_TAILS-1].col]='#'
        # knot_pos = np.full((GRID_SIZE,GRID_SIZE),'.')
        # for i in range(NUMBER_OF_TAILS):
        #     knot_pos[tks[i].row,tks[i].col] = str(i)
        # knot_pos[hk.row,hk.col] = 'H'
        # print (knot_pos)

# print ('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
# print (grid)
print (np.count_nonzero( grid =='#'))
