import sys
import numpy as np
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

class NoTreeInTheWayException(Exception):
    pass

lines = get_lines_from_file(day_number=8)

grid_width = len(strip_line(lines[0]))
grid_height = len(lines)

# top and bottom, and then the tree on left and tree on right of all other rows (hence -2)
trees_which_can_see_out = grid_width*2 + ((grid_height-2)*2)
print ("trees_which_can_see_out",trees_which_can_see_out)
grid_list = []
# Build Array
for line in lines:
    line = strip_line(line)
    line_list = list(line)
    line_list=list(map(int, line_list))
    grid_list.append(line_list)

tree_array = np.array(grid_list)
# Debug
print("Array tree_array is:\n",tree_array)
#type of tree_arrayrray
print("Type:", type(tree_array))
#Shape of array
print("Shape:", tree_array.shape)
#no. of dimensions
print("Rank:", tree_array.ndim)
#size of array
print("Size:", tree_array.size)
#type of each element in the array
print("Element type:", tree_array.dtype)

# Helper Methods
def is_outside_grid(row_index:int,col_index:int):
    if row_index<0 or col_index<0:
        return True
    if row_index>=grid_width:
        return True
    if col_index>=grid_height:
        return True
    return

def check_visible(tree_height:int,row_index:int,col_index:int,row_offset:int, col_offset:int):
    # Find first tree to check
    row_index += row_offset
    col_index += col_offset
    while not is_outside_grid(row_index,col_index):
        # print (f"TREE HEIGHT CHECK: row_index:{row_index} ,col_index:{col_index}, tree_height:{tree_array[row_index,col_index]}")
        if tree_height<=tree_array[row_index,col_index]:
            return
        row_index += row_offset
        col_index += col_offset

    raise NoTreeInTheWayException()
        


# Calculate visible treees
row_index = 1
while row_index < grid_height-1:
    col_index = 1
    while col_index < grid_width-1:
        tree_height = tree_array[row_index,col_index]
        try:
            # print ("===============================================")
            # print (f"IS VISIBLE: row_index:{row_index} ,col_index:{col_index}, tree_height:{tree_height}")
            # Check Up
            # print ("UP")
            check_visible(tree_height,row_index,col_index,row_offset = -1, col_offset = 0)
            # Check Down
            # print ("DOWN")
            check_visible(tree_height,row_index,col_index,row_offset = 1, col_offset = 0)
            # Check Left
            # print ("LEFT")
            check_visible(tree_height,row_index,col_index,row_offset = 0, col_offset = -1)
            # Check Right
            # print ("RIGHT")
            check_visible(tree_height,row_index,col_index,row_offset = 0, col_offset = 1)
        except NoTreeInTheWayException:
            trees_which_can_see_out += 1

        col_index +=1
    row_index+=1


print (trees_which_can_see_out)
"""
 [[3 0 3 7 3]
 [2 5 5 1 2]
 [6 5 3 3 2]
 [3 3 5 4 9]
 [3 5 3 9 0]]
"""