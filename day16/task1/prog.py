import sys
sys.path.append('..\..')
sys.path.append('..')

from file_lib import get_lines_from_file,strip_line,FileType
from structs import TreeNode,Status

day_number = 16
file_type:FileType = FileType.TestFile

lines = get_lines_from_file(day_number=day_number, file_type=file_type)
nodes:dict[str:TreeNode] = {}    
total_pressure_released =0

for line in lines:
    line = strip_line(line)
    inputs = line.replace(',','').replace(';','').replace('=',' ').split(' ')
    child_nodes:list[str] = []
    i = 10
    while i < len (inputs):
        child_nodes.append(inputs[i])
        i+=1
    nodes.update({inputs[1]:TreeNode(inputs[1],int(inputs[5]),child_nodes)})

for key,tree_node in nodes.items():
    for name in tree_node.child_node_names:
        tree_node.add_child_node(nodes[name])


def dfs_helper(minute:int, current_location:str, flow_rate:int, current_score:int, open_valves:set, nodes:dict[str:TreeNode],cache:dict)->int:
    if (minute > 30):
        return current_score
    
    cache_key = (minute,current_location,flow_rate)
    if cache_key in cache and cache[cache_key] > current_score:
        return None

    cache.update({cache_key:current_score})
    current_node:TreeNode = nodes[current_location]

    best_result_open_current:int = 0
    if current_node.pressure > 0 and current_location not in open_valves:
        new_open_valves = open_valves.copy()
        new_open_valves.add(current_location)
        new_score = current_score + flow_rate
        new_flow_rate =  flow_rate + current_node.pressure
        res = dfs_helper(minute+1,current_location,new_flow_rate,new_score,new_open_valves,nodes, cache)
        if res is not None:
            best_result_open_current = res
    print (minute,"best_result_open_current",best_result_open_current)
    best_result_down_tunnels:int = 0
    all_tunnels_result = {}
    for node_name in current_node.child_node_names:
        res = dfs_helper(minute+1, node_name, flow_rate, current_score+flow_rate, open_valves,nodes, cache)
        if res != None:
            all_tunnels_result.update({node_name:dfs_helper(minute+1, node_name, flow_rate, current_score+flow_rate, open_valves,nodes, cache)}) 
    if len(all_tunnels_result)>0:
        best_tunnel = max(all_tunnels_result)
        best_result_down_tunnels = all_tunnels_result[best_tunnel]
        print (minute,"best_tunnel",best_tunnel)
    print (minute,"best_result_down_tunnels",best_result_down_tunnels)

    res = max(best_result_down_tunnels,best_result_open_current)
    print (res)
    return max(best_result_down_tunnels,best_result_open_current)

def part1(nodes:dict[str:TreeNode]):
    cache:dict = {}
    open_valves = set()
    dfs_helper(1,"AA",0,0,open_valves,nodes,cache)


solutiuon1 = part1(nodes.copy())
