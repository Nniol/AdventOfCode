import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=4)

START_SHELF = 0
END_SHELF = 1

containing_lines = 0
for line in lines:
    ranges = strip_line(line).split(",")
    range1_str = ranges[0].split('-')
    range2_str = ranges[1].split('-')
    range1 =[int(range1_str[0]),int(range1_str[1])] 
    range2 =[int(range2_str[0]),int(range2_str[1])] 
    if (range1[START_SHELF] <= range2[START_SHELF] and range1[END_SHELF]>=range2[END_SHELF]):
        print (f"range1 {range1} contains range2 {range2}")
        containing_lines+=1
    elif (range2[START_SHELF] <= range1[START_SHELF] and range2[END_SHELF]>=range1[END_SHELF] ):
        print (f"range2 {range2} contains range1 {range1}")
        containing_lines+=1

print (containing_lines)