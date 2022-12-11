import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

COMMAND_COUNT:int = 1
COMMAND_FROM:int = 3
COMMAND_TO:int = 5

class StackOfCubes():

    def __init__(self, cubes: str):
        self._cubes: list[chr] = []
        cube_list = cubes.split(",")
        for cube in cube_list:
            self.add_cube(cube)

    def add_cube(self,cube:chr):
        self._cubes.append(cube)

    def get_top_cube(self)->chr:
        return self._cubes.pop()

    def __str__(self):
        return str(self._cubes)

"""
[M]                     [N] [Z]    
[F]             [R] [Z] [C] [C]    
[C]     [V]     [L] [N] [G] [V]    
[W]     [L]     [T] [H] [V] [F] [H]
[T]     [T] [W] [F] [B] [P] [J] [L]
[D] [L] [H] [J] [C] [G] [S] [R] [M]
[L] [B] [C] [P] [S] [D] [M] [Q] [P]
[B] [N] [J] [S] [Z] [W] [F] [W] [R]
"""
warehouse_real: dict = {
    "1": StackOfCubes('B,L,D,T,W,C,F,M'),
    "2": StackOfCubes('N,B,L'),
    "3": StackOfCubes('J,C,H,T,L,V'),
    "4": StackOfCubes('S,P,J,W'),
    "5": StackOfCubes('Z,S,C,F,T,L,R'),
    "6": StackOfCubes('W,D,G,B,H,N,Z'),
    "7": StackOfCubes('F,M,S,P,V,G,C,N'),
    "8": StackOfCubes('W,Q,R,J,F,V,C,Z'),
    "9": StackOfCubes('R,P,M,L,H')
}

"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 """
warehouse_tst:dict = {
    "1": StackOfCubes('Z,N'),
    "2": StackOfCubes('M,C,D'),
    "3": StackOfCubes('P'),
}

def print_warehouse(warehouse:dict):
    for key in warehouse.keys():
        print (f"{str(key)}: {warehouse[key]}")

lines = get_lines_from_file(day_number=4)
warehouse = warehouse_real
for line in lines:
    command = strip_line(line).split(' ') 
    if command[0]!="move":
        continue
    for i in range(int(command[COMMAND_COUNT])):
        from_stack = command[COMMAND_FROM]
        to_stack = command[COMMAND_TO]
        warehouse[to_stack].add_cube(warehouse[from_stack].get_top_cube())
    print_warehouse(warehouse)

stack = 0
ret_str = ""
while stack  < len(warehouse):
    ret_str += warehouse[str(stack+1)].get_top_cube()
    stack +=1

print (ret_str)
