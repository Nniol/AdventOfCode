import sys
import os
from structs import ElfInfo

sys.path.append('..\..')

from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=1)

elves = dict()
most_calories = 0
current_elf = None
current_elf_num = 1

elves: list[ElfInfo] = []

def get_total_calories(elf:ElfInfo)->int:
    return elf.total_caloris

for line in lines:
    line = strip_line(line)
    if current_elf is None:
        current_elf = ElfInfo(number=current_elf_num, count_food_items=0,total_caloris=0)
    if line == "":
        current_elf_num += 1
        print (f"elf#[{current_elf.number}] #food_items[{current_elf.count_food_items}] total_calories:[{current_elf.total_caloris}]")
        if current_elf.total_caloris > most_calories:
            most_calories = current_elf.total_caloris
        elves.append(current_elf)
        current_elf = None
        continue
    current_elf.count_food_items = current_elf.count_food_items+1
    current_elf.total_caloris += int(line)
elves.sort(key=get_total_calories,reverse=True)
top_3_elves = elves[:3]
print (top_3_elves)
print (os.linesep)
total_calories_top_3 = 0
for elf in top_3_elves:
    total_calories_top_3 += elf.total_caloris

print (total_calories_top_3)
