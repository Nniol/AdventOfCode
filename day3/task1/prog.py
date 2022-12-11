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
for line in lines:
    line = strip_line(line)
    compartment_contents = split_string(line)
    for item in compartment_contents[0]:
        try:
            compartment_contents[1].index(item)
        except ValueError:
            continue # Not found so just keep looking
        ascii_val = ord(item)
        if item.isupper():
            pri= ascii_val-38 # A is ASCII 65, 65 -38 gives 27 which is the priority of A
        else:
            pri =ascii_val-96 # a is ASCII 97, 97 -96 gives 27 which is the priority of A
        print (f"Line [{line_no}] Common item: [{item }] Priority[{pri}]")
        total_pri += pri
        break # do next line

    line_no +=1

print (total_pri)
