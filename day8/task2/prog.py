import sys
import numpy as np
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=8)

grid_width = len(strip_line(lines[0]))
grid_height = len(lines)

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

def count_visible_trees(tree_height:int,row_index:int,col_index:int,row_offset:int, col_offset:int)->int:
    # Find first tree to check
    row_index += row_offset
    col_index += col_offset
    seen_trees = 0
    while not is_outside_grid(row_index,col_index):
        # print (f"TREE HEIGHT CHECK: row_index:{row_index} ,col_index:{col_index}, tree_height:{tree_array[row_index,col_index]}")
        seen_trees +=1
        if tree_height<=tree_array[row_index,col_index]:
            return seen_trees
        row_index += row_offset
        col_index += col_offset

    return seen_trees
        


# Calculate visible treees
row_index = 1
max_scenic_score = 0
while row_index < grid_height-1:
    col_index = 1
    while col_index < grid_width-1:
        tree_height = tree_array[row_index,col_index]
        scenic_score = 1
        # print ("===============================================")
        # print (f"TREE COUNT: row_index:{row_index} ,col_index:{col_index}, tree_height:{tree_height}")
        # Check Up
        # print ("UP")
        scenic_score *= count_visible_trees(tree_height,row_index,col_index,row_offset = -1, col_offset = 0)
        # Check Down
        # print ("DOWN")
        scenic_score *= count_visible_trees(tree_height,row_index,col_index,row_offset = 1, col_offset = 0)
        # Check Left
        # print ("LEFT")
        scenic_score *= count_visible_trees(tree_height,row_index,col_index,row_offset = 0, col_offset = -1)
        # Check Right
        # print ("RIGHT")
        scenic_score *= count_visible_trees(tree_height,row_index,col_index,row_offset = 0, col_offset = 1)
        # print ("scenic_score",scenic_score)
        if scenic_score > max_scenic_score:
            print(f"New Max Scenic Score {scenic_score} location({row_index},{col_index})")
            max_scenic_score = scenic_score

        col_index +=1
    row_index+=1


print (max_scenic_score)
"""
 [[3 0 3 7 3]
 [2 5 5 1 2]
 [6 5 3 3 2]
 [3 3 5 4 9]
 [3 5 3 9 0]]
"""