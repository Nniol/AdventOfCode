from collections import namedtuple

GraphVertex = namedtuple('GraphVertex',['node_key','distance','direction'])


class Coord():

    def __init__(self,x:int,y:int,height:int=0,dist:int=0,direction_char:str='') -> None:
        self.x: int = x
        self.y: int = y
        self.height: int=height
        self.direction_char = direction_char
        self.next_nodes:list = []

    def get_node_key(self)->str:
        return f"{self.x}_{self.y}"

    
    def __str__(self) -> str:
        return f"x:{self.x}; y:{self.y}: height:{self.height}; distance:{self.dist}"

    def add_next_node(self, node_key:str,direction:str):
        self.next_nodes.append(GraphVertex(node_key,1,direction))

