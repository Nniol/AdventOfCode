from enum import Enum
from collections import namedtuple
import numpy as np

Offset = namedtuple('Offset',['x','y'])

class PointType(Enum):
    NOT_COVERED:str = '.'
    COVERED: str = '#'
    BEACON: str = 'B'
    SENSOR: str = 'S'


class Point():

    def __init__(self, x:int, y:int, point_type:PointType) -> None:
        self.x :int = x
        self.y :int = y
        self.type:PointType = point_type
        self.nearest_beacon: Point = None
        self.distance_to_beacon: int = 0

    def set_beacon(self,beacon)->None:
        self.nearest_beacon = beacon
        self.distance_to_beacon = self.get_distance_to(self.nearest_beacon)

    def is_closer_or_equal_to_beacon(self,point) -> bool:
        return self.get_distance_to(point) <= self.distance_to_beacon
        
    def is_covered(self):
        return self.type.value in [PointType.COVERED.value, PointType.BEACON.value, PointType.SENSOR.value]

    def set_covered(self):
        self.type = PointType.COVERED

    def get_dict_key(self):
        return f'{self.x}_{self.y}'

    def get_distance_to(self, point) -> int:
        return abs(self.x - point.x) + abs(self.y - point.y)
        
    def __str__(self)->str:
        ret_str = f"{self.x},{self.y}: {self.type} covered:{self.is_covered()}"
        if self.type.value is PointType.SENSOR.value:
            ret_str += f" distance:{self.distance_to_beacon}: {self.nearest_beacon}"
        return ret_str


class Grid():

    GRID_MIN_X:int = 0
    GRID_MAX_X:int = 0
    GRID_MIN_Y:int = 0
    GRID_MAX_Y:int = 0
    GRID_WIDTH: int = 0
    GRID_HEIGHT:int = 0 
    __grid = None
    LINE_PADDING = '    '
    PADDING = ' '

    @staticmethod
    def build_grid():
        Grid.__grid = np.full((Grid.GRID_HEIGHT, Grid.GRID_WIDTH),None)

    @staticmethod
    def add_point(p: Point):
        grid_x = p.x - Grid.GRID_MIN_X
        grid_y = p.y - Grid.GRID_MIN_Y
        Grid.__grid[grid_y][grid_x] = p

    @staticmethod
    def calculate_dimensions():
        Grid.GRID_HEIGHT = (Grid.GRID_MAX_Y - Grid.GRID_MIN_Y)+1
        Grid.GRID_WIDTH = (Grid.GRID_MAX_X - Grid.GRID_MIN_X)+1

    @staticmethod
    def count_covered(test_y: int)->int:
        count = 0
        for test_x in range(Grid.GRID_WIDTH):
            if Grid.__grid[test_y][test_x].type.value == PointType.COVERED.value:
                count += 1
        return count

    @staticmethod
    def point_on_grid(p: Point) -> bool:
        grid_x = p.x - Grid.GRID_MIN_X
        grid_y = p.y - Grid.GRID_MIN_Y
        if grid_x >= 0 and grid_x < Grid.GRID_WIDTH and \
            grid_y >= 0 and grid_y < Grid.GRID_HEIGHT:
                return True
        return False

    @staticmethod
    def point_is_not_covered(p: Point) -> bool:
        grid_x = p.x - Grid.GRID_MIN_X
        grid_y = p.y - Grid.GRID_MIN_Y
        grid_p:Point = Grid.__grid[grid_y][grid_x]
        return grid_p == None or not grid_p.is_covered()

    @staticmethod
    def print_grid():
        print ()
        line=Grid.LINE_PADDING
        for i in range (Grid.GRID_WIDTH):
            i += Grid.GRID_MIN_X
            if i % 5 == 0 and int(i / 10) > 0:
                line += f'{int(i / 10)}'
            else:
                line += ' '
        print (line)
        line=Grid.LINE_PADDING
        for i in range (Grid.GRID_WIDTH):
            i += Grid.GRID_MIN_X
            if i % 5 == 0:
                if i % 10 == 0:
                    line += '0'
                else:
                    line += '5'
            else:
                line += ' '
        print (line)
        for y in range(Grid.GRID_HEIGHT):
            y += Grid.GRID_MIN_Y
            line = ""
            line += f"{str(y):{Grid.PADDING}>3} "
            for x in range (Grid.GRID_WIDTH):
                if Grid.__grid[y,x]==None:
                    line += '.'
                else:
                    line += Grid.__grid[y,x].type.value
            print (line)


    @staticmethod
    def check_min_max(p: Point):
        if p.x < Grid.GRID_MIN_X:
            Grid.GRID_MIN_X = p.x
        elif p.x > Grid.GRID_MAX_X:
            Grid.GRID_MAX_X = p.x

        if p.y < Grid.GRID_MIN_Y:
            Grid.GRID_MIN_Y = p.y
        elif p.y > Grid.GRID_MAX_Y:
            Grid.GRID_MAX_Y = p.y
