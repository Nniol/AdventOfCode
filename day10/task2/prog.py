import sys
from collections import namedtuple
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line
from structs import Command,CMD_NO_OPERATION,CMD_ADDX,CMD_BOOTUP,Operation,CPU
lines = get_lines_from_file(day_number=10)

my_cpu = CPU(init_reg_x_value= 1)

for line in lines:
    line:str = strip_line(line)
    command: list[str] = line.split(' ')
    parameter:int | None = None
    cmd:Command = my_cpu.parse(command[0])
    if len(command)>1:
        parameter = int(command[1]) 
    my_cpu.execute_command(cmd,parameter)

intervals = [20,60,100,140,180,220]
total = 0
for i in intervals:
    print (i,my_cpu.get_reg_x_value(i),':',i * my_cpu.get_reg_x_value(i))
    total += i * my_cpu.get_reg_x_value(i) 

print (total)
# print (CPU._reg_x_history)
print (CPU.CRT)