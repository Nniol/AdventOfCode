import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=3)
total_pri = 0

def split_string(string):
    string_len = len(string)
    half_len = string_len//2
    first_half = string[0:half_len]
    second_half = string[half_len:]
    return [first_half,second_half]
line_no = 1
group_no = 1
group_contents:list[str] = []
for line in lines:
    index = line_no % 3 
    group_contents.append(strip_line(line))
    if index == 0:
        # Calculate badge and pri
        for item in group_contents[0]:
            try:
                group_contents[1].index(item)
                group_contents[2].index(item)
            except ValueError:
                continue
            # onlt get here is all item exist in all three bas
            ascii_val = ord(item)
            if item.isupper():
                pri= ascii_val-38 # A is ASCII 65, 65 -38 gives 27 which is the priority of A
            else:
                pri =ascii_val-96 # a is ASCII 97, 97 -96 gives 27 which is the priority of A
            print (f"Group[{group_no}] Common item: [{item }] Priority[{pri}]")
            total_pri += pri
            break # do next line
        # reset array and do again
        group_contents = []
        group_no += 1
    line_no+=1





print (total_pri)
