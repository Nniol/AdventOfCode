import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line
from structs import Monkey
lines = get_lines_from_file(day_number=11)

test_monkeys:dict[int,Monkey] = {
    0: Monkey([79, 98],"old * 19",23,(3,2),True),
    1: Monkey([54, 65, 75, 74],"old + 6",19,(0,2),True),
    2: Monkey([79, 60, 97],"old * old",13,(3,1),True),
    3: Monkey([74],"old + 3",17,(1,0),True)
}

real_monkeys:dict[int,Monkey] = {
    0: Monkey([99, 63, 76, 93, 54, 73],"old * 11",2,(1,7),True),
    1: Monkey([91, 60, 97, 54],"old + 1",17,(2,3),True),
    2: Monkey([65],"old + 7",7,(5,6),True),
    3: Monkey([84, 55],"old + 3",11,(6,2),True),
    4: Monkey([86, 63, 79, 54, 83],"old * old",19,(0,7),True),
    5: Monkey([96, 67, 56, 95, 64, 69, 96],"old + 4",5,(0,4),True),
    6: Monkey([66, 94, 70, 93, 72, 67, 88, 51],"old * 5",13,(5,4),True),
    7: Monkey([59, 59, 74],"old + 8",3,(3,1),True)
}

monkeys:dict[int,Monkey] = real_monkeys
super_mod = 1
for key,monkey in monkeys.items():
    super_mod *= monkey._div_by_number

MONKEY_ID = 0
WORRY_ID = 1
NUM_ROUNDS = 10000 

for i in range(NUM_ROUNDS):
    for key,monkey in monkeys.items():
        # print ("#",key)
        monkey.set_supermod(supermod=super_mod)
        while monkey.has_items():
            # print ("================")
            pass_to:tuple = monkey.inspect_item()
            monkeys[pass_to[MONKEY_ID]].add_item(pass_to[WORRY_ID])
        # print ()
        # print ()

# using items() to get all items 
# lambda function is passed in key to perform sort by key 
# passing 2nd element of items()
# adding "reversed = True" for reversed order
busiest_monkeys = {key: val for key, val in sorted(monkeys.items(), key = lambda ele:ele[1]._inspects, reverse=True)}

for key,monkey in busiest_monkeys.items():
    print(key,monkey._inspects)

tot = 1
count = 0
for key,monkey in busiest_monkeys.items():
    tot *= monkey._inspects
    count += 1
    if count >= 2:
        break

print (tot)
