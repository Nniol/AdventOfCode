class Coord():

    def __init__(self,x:int,y:int,height:int=0,dist:int=0,replacement_char:str = None) -> None:
        self.x: int = x
        self.y: int = y
        self.height: int=height
        self.dist: int = dist
        self.replacement_char=replacement_char

    def get_node_key(self)->str:
        return f"{self.x}_{self.y}"

    def __str__(self) -> str:
        return f"x:{self.x}; y:{self.y}: height:{self.height}; distance:{self.dist}"

    def copy(self):
        return Coord(self.x,self.y,self.height)

