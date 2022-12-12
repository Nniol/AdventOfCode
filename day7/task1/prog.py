import sys
sys.path.append('..\..')
sys.path.append('..')
from structs import CommDir
from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=7)

ROOT_COMM_DIR:CommDir = CommDir('root',None)
current_dir:CommDir = ROOT_COMM_DIR

COMMAND_ACTION = '$'
DIRECTORY_NAME = 'dir'

CHANGE_DIR_COMMAND = 'cd'
LIST_DIR_COMMAND = 'ls'

PREVIOUS_DIR_FILE = '..'

TOTAL_DISK_SIZE:int = 70000000
SPACE_FOR_UDPATE:int = 30000000

for line in lines:
    line = strip_line(line)

    commands = line.split(' ')
    print (commands)
    if commands[0]==COMMAND_ACTION:
        if commands[1]==CHANGE_DIR_COMMAND:
            if commands[2] == '/':
                current_dir = ROOT_COMM_DIR
            elif commands[2] == PREVIOUS_DIR_FILE:
                current_dir = current_dir.get_parent()
            else:
                current_dir = current_dir.getdir(commands[2])

        # elif commands[1]==LIST_DIR_COMMAND:
            # Do nothing
    elif commands[0] == DIRECTORY_NAME:
            current_dir.mkdir(commands[1])
    else: # numeric value, file size
        current_dir.addfile(commands[1],int(commands[0]))

free_space = TOTAL_DISK_SIZE - ROOT_COMM_DIR.size
space_needed = SPACE_FOR_UDPATE - free_space

print (ROOT_COMM_DIR.list_contents(0))
print (ROOT_COMM_DIR.count_size_dirs_under(100000))
print (f"{TOTAL_DISK_SIZE} - {ROOT_COMM_DIR.size}: {free_space}")
print (f"{SPACE_FOR_UDPATE} - {free_space}: {space_needed}")
print (ROOT_COMM_DIR.find_nearest_over(space_needed,ROOT_COMM_DIR.size))


