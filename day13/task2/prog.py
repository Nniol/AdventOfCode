import ast
import sys
import numpy as np
import re
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line

lines = get_lines_from_file(day_number=13)

class Packet():

    def __init__(self,p_str:str) -> None:
        self.packet_as_str:str = p_str
        self.packet_as_arr = ast.literal_eval(self.packet_as_str)

        self.list_as_numbers = self.calc_list_as_numbers(p_str)

    def calc_list_as_numbers(self,p_str:str):
        ret_list:list = []
        i = 0
        nest_level_found=[]
        while i < len(p_str):
            chr = p_str[i]
            if chr.isdigit():
                t_num = chr
                extend_i=1
                while p_str[i+extend_i].isdigit():
                    t_num += p_str[i+extend_i]
                    extend_i+=1
                ret_list.append(int(t_num))
                i+= extend_i-1
                for k in range(len(nest_level_found)):
                    nest_level_found[k] = True
            elif chr == '[':
                # is it next to a close
                if p_str[i+1]==']': # closes immediately so no need to keeo tabs
                    ret_list.append(-1)
                    i+=1 # Skip the ']' 
                else:
                    nest_level_found.append(False)
            elif chr == ']':
                if nest_level_found[len(nest_level_found)-1]==False:
                    ret_list.append(-1)
                # Closed a nest level, remove the found trigger
                nest_level_found.pop()
            i += 1                

        return ret_list

    def __str__(self) -> str:
        return (f"str:{self.packet_as_str}; arr:{self.packet_as_arr}; numbers:{self.list_as_numbers};")

def compare_packets_as_numbers(p1:list, p2:list)->bool:
    while True:
        # if len(p1)==0 or len(p2)==0:
        #     print ("Nothing left in one or the rother mhavenät had a succesfuk greater than so is false")
        #     return False
        if len(p1)==0 and len(p2)>0: # p1 is out but not p2, p1 less than p2
            # print ("P2 remaining, p1 out: p1 LESS THAN")
            return False
        if len(p1)>0 and len(p2)==0: # p1 has things and but not p2, p1 more than p2
            # print ("P1 remaining, p2 out: p1 MORE THAN")
            return True
        if len(p1)==0 and len(p2)==0:# both out at same time equals
            # print ("EQUAL LENGHTS; False")
            return False
        val1 = p1.pop(0)
        val2 = p2.pop(0)
        # print (val1,val2)
        if val1 > val2:
            # print ("Return: True")
            return True
        if val2 > val1:
            # print ("Return: False")
            return False
            

def bubble_sort(dict1:dict[int,Packet]):  
    n = len(dict1)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            grt_thn = False
            j_numbers = dict1[j].list_as_numbers.copy()
            j1_numbers = dict1[j+1].list_as_numbers.copy()
            grt_thn = compare_packets_as_numbers(j_numbers,j1_numbers)
            if grt_thn:
                swapped = True
                dict1[j], dict1[j + 1] = dict1[j + 1], dict1[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

packet_dict:dict[int,Packet] = {}
index = 0
for line in lines:
    line = strip_line(line)
    if len(line)>0:
        packet =Packet(line)
        packet_dict.update({index:packet})
        index += 1

# Add dividers
packet_dict.update({index:Packet("[[2]]")})
packet_dict.update({index+1:Packet("[[6]]")})
# for key,value in packet_dict.items():
#     print (key,value.list_as_numbers)

bubble_sort(packet_dict)
# Find first three
found_div_2 = 0
found_div_6 = 0
for key,value in packet_dict.items():
    # print (key,value.packet_as_str,value.list_as_numbers)
    if found_div_2==0 and value.packet_as_str=="[[2]]":
        div_2_ind = key +1 # Add 1 as we start at 0
    if found_div_6==0 and value.packet_as_str=="[[6]]":
        found_div_6 = key +1 # Add 1 as we start at 0

print (div_2_ind,found_div_6, div_2_ind*found_div_6)


    

