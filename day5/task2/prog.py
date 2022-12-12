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

    def add_cubes(self,cubes:list[chr]):
        self._cubes.extend(cubes)

    def get_top_cube(self)->chr:
        if len(self._cubes)>0:
            return self._cubes.pop()
        return ""

    def get_top_cubes(self,cubes_to_moves:int)->chr:
        ret_list = self._cubes[-cubes_to_move:]
        self._cubes = self._cubes[:len(self._cubes)-cubes_to_moves]
        return ret_list

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

lines = get_lines_from_file(day_number=5)
warehouse = warehouse_real
print_warehouse(warehouse)
for line in lines:
    command = strip_line(line).split(' ') 
    if command[0]!="move":
        continue
    cubes_to_move = int(command[COMMAND_COUNT])
    from_stack = command[COMMAND_FROM]
    to_stack = command[COMMAND_TO]
    moving_cubes = warehouse[from_stack].get_top_cubes(cubes_to_move)
    print (f"move {cubes_to_move}: {moving_cubes} from {from_stack} to {to_stack}")
    warehouse[to_stack].add_cubes(moving_cubes)
    print_warehouse(warehouse)

stack = 0
ret_str = ""
while stack  < len(warehouse):
    ret_str += warehouse[str(stack+1)].get_top_cube()
    stack +=1

print (ret_str)
