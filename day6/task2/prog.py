import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=6)

def find_dup_char(input)->set:
    x:filter = filter(lambda x: input.count(x) >= 2, input)
    return set(x)
    # print(' '.join(set(x)))


for line in lines:
    line = strip_line(line)
    print(line)
    start_index = 0
    while start_index + 14 < len(line):
        four_chars = line[start_index:start_index+14]
        dups = find_dup_char(four_chars)
        if len(dups)==0:
            break
        start_index+=1

    print (start_index+14)


