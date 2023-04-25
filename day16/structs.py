import os

from enum import Enum


class Status(Enum):
    MOVING:str = "MOVING"
    OPENING:str = "OPENING"
    DECISION:str = "STILL"

class ValveState(Enum):
    OPEN:int =1
    CLOSED:int = 0

class TreeNode():

    NODES_VISITED:list=[]

    def __init__(self,node_name:str,pressure:int,child_node_names:list[str]) -> None:
        self.node_name:str = node_name
        self.pressure:int = pressure
        self.child_node_names:list[str] = child_node_names
        self.current_weight:int = 0
        self.child_nodes:list = [] # Gets filled after have all the names
        self.parent_node = None
        self.valve_open: ValveState = ValveState.CLOSED

    def add_child_node(self, child_node):
        self.child_nodes.append(child_node)

    def close_valve(self):
        self.valve_open = ValveState.CLOSED

    def calculate_weights(self,minutes_left:int,reset_nodes_visited:bool = True,pre_visited:list[str]=[]) -> int:
        if reset_nodes_visited:
            # print ("RESET NODE")
            TreeNode.NODES_VISITED = []
        TreeNode.NODES_VISITED.extend(pre_visited)
        if self.node_name in TreeNode.NODES_VISITED:
            return 0
        if minutes_left <= 0:
            return 0
        TreeNode.NODES_VISITED.append(self.node_name)
        self.current_weight = 0
        if self.valve_open.name == ValveState.CLOSED.name: # Open Valves add no weight as they will always add weight
            # If we open the valve it will take 1 minute so need to get two trees and work out which is best, open or not open
            open_weight = self.pressure * minutes_left-1 # Takes a minute to open the valve
            closed_weight = 0
            for child_node in self.child_nodes:
                open_weight += child_node.calculate_weights(minutes_left-2,False)
                closed_weight += child_node.calculate_weights(minutes_left-1,False)
            self.current_weight = max(open_weight,closed_weight)
        else:
            for child_node in self.child_nodes:
                self.current_weight += child_node.calculate_weights(minutes_left-2,False)
        # print (self.node_name,minutes_left,self.valve_open.name,self.pressure,self.current_weight)
        return self.current_weight

    def calculate_pressure_for_a_minute(self,reset_nodes_visited:bool = True) -> int:
        if reset_nodes_visited:
            TreeNode.NODES_VISITED = []
        if self.node_name in TreeNode.NODES_VISITED:
            return 0
        TreeNode.NODES_VISITED.append(self.node_name)
        pressure = 0
        if self.valve_open.name == ValveState.OPEN.name:
            pressure += self.pressure
        for child_node in self.child_nodes:
            pressure += child_node.calculate_pressure_for_a_minute(False)
        self.current_weight = 0 # Reset
        return pressure


    def open_valve(self,):
        self.valve_open = ValveState.OPEN

    def __str__(self) -> str:
        return f'{self.node_name}: {self.pressure}; {self.child_node_names}'

    def print_tree(self,indent:int = 0) -> str:
        if indent==0:
            TreeNode.NODES_VISITED = []
        if self.node_name in TreeNode.NODES_VISITED:
            return f'{chr(9) * indent}{self.node_name}: {self.current_weight}{os.linesep}'

        TreeNode.NODES_VISITED.append(self.node_name)
        ret_str =  f'{chr(9) * indent}{self.node_name}: {self.current_weight}{os.linesep}'
        for child in self.child_nodes:
            ret_str += child.print_tree(indent+1)
        return ret_str