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
    range1:range =range(int(range1_str[0]),int(range1_str[1])+1)
    range2:range =range(int(range2_str[0]),int(range2_str[1])+1)
    # print (range1.start,range1.stop,range2.start,range2.stop)
    overlap = range(max(range1.start, range2.start), min(range1.stop, range2.stop))
    if len(overlap)>0:
        print (range1_str,range1_str,overlap)
        containing_lines+=1
    else:
        print (range1_str,range2_str)



print (containing_lines)