from collections import namedtuple
MonkeyPass = namedtuple('MonkeyPass',['monkey_number','worry'])



class Monkey():

    def __init__(self,starting_items:list[int],operation:str,test:int,pass_to_monkey:tuple) -> None:
        self._items =starting_items
        self._items = starting_items
        self._div_by_number = test
        self._operation = operation
        self._pass_to_monkey:tuple = pass_to_monkey # Tuple, index 0 is for False, Index 1 is for Tue

        self._inspects = 0

    def has_items(self):
        return len(self._items) != 0

    def inspect_item(self):
        # inspect
        old = self._items.pop(0)
        # print (old)
        self._inspects += 1
        new = eval(self._operation)
        # new = int(new / 3)
        # print (new)
        pass_to =   new % self._div_by_number == 0
        # print (pass_to)
        mp= MonkeyPass(monkey_number=self._pass_to_monkey[pass_to],worry=new)
        # print (mp)
        return mp

    def add_item(self,worry:int):
        self._items.append(worry)

    def __str__(self) -> str:
        return f"items:{self._items}, inspects:{self._inspects}"


