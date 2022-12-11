import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line
from structs import rps_round
lines = get_lines_from_file(day_number=2)
total_points = 0

for line in lines:
    line = strip_line(line)
    shape_codes = line.split(' ')
    print (f"{shape_codes[0]}:{shape_codes[1]}")
    round = rps_round(opp_shape_code=shape_codes[0],my_code=shape_codes[1])
    total_points += round.play()


print (total_points)