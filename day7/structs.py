import os

class CommFile():

    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size



class CommDir():

    def __init__(self, name:str, parent_dir):
        self.name = name
        self.size = 0
        self.parent:CommDir = parent_dir
        self.dirs: dict[str,CommDir]={}
        self.files: dict[str,CommFile]={}

    def getdir(self,name:str):
        if name not in self.dirs:
            self.mkdir(name)
        return self.dirs[name]

    def mkdir(self, name:str):
        self.dirs[name] = CommDir(name,self)

    def addfile(self,name:str,size:int):
        self.files[name] = CommFile(name,size)
        self.size += size
        if self.parent != None:
            self.parent.inherit_file_size(size)

    def get_parent(self):
        return self.parent

    def inherit_file_size(self, size:int):
        self.size += size
        if self.parent != None:
            self.parent.inherit_file_size(size)

    def list_contents(self,indent:int) -> str:
        indent_str ='\t'*indent
        str = f"{indent_str}{self.name} - {self.size}{os.linesep}"
        for key,value in self.dirs.items():
            str += value.list_contents(indent+1)
        for key,value in self.files.items():
            str += f"{indent_str}{value.size} {value.name}{os.linesep}"

        return str

    def count_size_dirs_under(self,max_size:int) -> int:
        total_size = 0
        if self.size<=max_size:
            total_size += self.size
        for key,value in self.dirs.items():
            total_size += value.count_size_dirs_under(max_size)

        return total_size

    def find_nearest_over(self,minimum_size:int,current_lowest:int)->int:
        if self.size > minimum_size and self.size<current_lowest:
            current_lowest = self.size
        for key,value in self.dirs.items():
            current_lowest = value.find_nearest_over(minimum_size,current_lowest)
        return current_lowest


            