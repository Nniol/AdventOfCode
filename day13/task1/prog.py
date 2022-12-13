import ast
import sys
from enum import Enum 
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=13)

UNKNOWN:int = -1
CORRECT:bool = True
WRONG:bool = False

def perform_check(p1:list, p2:list):
    # print ("INPUT\r\n",p1,":",p2)
    state=UNKNOWN
    while state == UNKNOWN:
        if len(p1)==0 and len(p2)>0: # p1 is out but not p2, this is ok
            # print ("P1 Out, p2 has remaining: CORRECT")
            return CORRECT
        if len(p1)>0 and len(p2)==0: # p1 has things and but not p2, this is not OK
            # print ("P1 remaining, p2 out: WRONG")
            return WRONG
        if len(p1)==0 and len(p2)==0:# both out at same time this is not OK
            # print ("EQUAL LENGHTS; UNKOWN")
            return UNKNOWN

        val1 = p1.pop(0)
        val2 = p2.pop(0)
        # print ("Popped Vals:",val1,val2)
        if isinstance(val1,int) and isinstance(val2,int):
            # print ("INTEGER,INTEGER")
            if val1 < val2:
                state = CORRECT
            elif val1 > val2:
                state = WRONG
        elif isinstance(val1,list) and isinstance(val2,list):
            # print ("LIST,LIST")
            state = perform_check(val1,val2)
        elif isinstance(val1,int):
            # print ("INTEGER,LIST")
            state = perform_check([val1],val2)
        else: # val2 must be an int and val1 a list
            # print ("LIST,INTEGER")
            state = perform_check(val1,[val2])
        # print ("state",state,state!=UNKNOWN)
        if state != UNKNOWN:
            # print ("RETURNING:",state)
            return state

pair_index=1
ok_pair_total=0
while len(lines)>0:
    p1 = lines.pop(0)
    p2 = lines.pop(0)

    p1 =ast.literal_eval(p1)
    p2 =ast.literal_eval(p2)

    if perform_check(p1,p2):
        ok_pair_total += pair_index

    pair_index+=1

    if len(lines)>0:
        lines.pop(0) # Pop blank line


print (ok_pair_total)

