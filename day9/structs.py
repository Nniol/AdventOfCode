import os
from collections import namedtuple

Offset = namedtuple('Offset',['row','col'])


class KnotPos():

    def __init__(self, row:int, col:int):
        self.row = row
        self.col = col

    def move(self,offset:Offset):
        self.row += offset.row
        self.col += offset.col

    def __str__(self) -> str:
        return f"[{self.row},{self.col}]"
