
import os
import sys
from pathlib import Path



def get_lines_from_file(day_number:str) -> list[str]:
    input_path = Path(__file__).parent
    input_path = Path(f"{str(input_path)}{os.sep}day{day_number}{os.sep}inputFile.txt")

    input_file = open(input_path,"r")
    return input_file.readlines()


def strip_line(line:str)->str:
    line=line.replace('\n','')
    line=line.replace('\r','')
    line=line.replace('\t','')
    return line