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

# print(nodes['AA'].print_tree())
MAX_MINUTES = 30
STATUS = Status.DECISION
current_node:TreeNode = nodes['AA']
minutes_left = 30
while minutes_left >0 :
    print ("minute",(MAX_MINUTES - minutes_left)+1,STATUS.name, current_node.node_name)
    if STATUS.name == Status.DECISION.name: # What do we do: Open or Movemax_weight
        print ("Calc. Weights")
        for node in current_node.child_nodes:      
            node.calculate_weights(minutes_left-1,pre_visited=[current_node.node_name]) # Time taken to move there
        new_node:TreeNode = None
        max_weight = 0
        for node in current_node.child_nodes:
            print (node.node_name,node.current_weight,max_weight)
            if node.current_weight > max_weight:
                max_weight = node.current_weight
                new_node = node
        print (new_node.node_name,new_node.current_weight,max_weight)
        if not current_node.valve_open.value: # weight is pressure * minutes minus time to open
            current_node.current_weight = current_node.pressure * (minutes_left-1)
            print (current_node.pressure,'*',minutes_left-1,'=',current_node.pressure * (minutes_left-1))
        else: # Already open, so no need to open it now
            current_node.current_weight = 0
        print ("Calcs:",current_node.node_name,current_node.current_weight,max_weight,(current_node.current_weight + max_weight),(current_node.current_weight + max_weight) > max_weight)
        if (current_node.current_weight + max_weight) > max_weight:
            print (f"Opening: {current_node.node_name}")
            STATUS = Status.OPENING
        else:
            print (f"moving to: {new_node.node_name}")
            current_node = new_node
            STATUS = Status.MOVING
        pressure_released = nodes['AA'].calculate_pressure_for_a_minute()
        print (f"Pressure release: {pressure_released}")
        total_pressure_released += pressure_released
    elif STATUS == Status.MOVING:
        total_pressure_released += nodes['AA'].calculate_pressure_for_a_minute()
        STATUS = Status.DECISION
        minutes_left -= 1
    else: # Status is OPENING
        total_pressure_released += nodes['AA'].calculate_pressure_for_a_minute()
        current_node.open_valve()       
        STATUS = Status.DECISION
        minutes_left -= 1
    # print (current_node.print_tree())

print (total_pressure_released)