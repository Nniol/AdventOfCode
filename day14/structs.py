class Coord():

    def __init__(self,x:int,y:int) -> None:
        self.x :int= x
        self.y :int = y

    def __str__(self) -> str:
        return f"x:{self.x}; y:{self.y}"

    def copy(self):
        return Coord(self.x,self.y)

