from collections import namedtuple
import numpy as np
Offset = namedtuple('Offset',['row','col'])

Command = namedtuple('Command',['code','cycles_to_complete'])

CMD_BOOTUP = Command(code='STARTUP',cycles_to_complete=0)
CMD_NO_OPERATION =  Command(code='noop',cycles_to_complete=1)
CMD_ADDX =  Command(code='addx',cycles_to_complete=2)

class Operation():

    def __init__(self,cmd:Command, parameter:int = None) -> None:
        self._cmd : Command= cmd
        self._parameter:int | None = parameter
        self._cycles_to_complete = self._cmd.cycles_to_complete
        print (f"Operation {self._cmd.code}, parameter {self._parameter}, cycles to complete {self._cycles_to_complete}")

    def execute_cycle(self):
        self._cycles_to_complete-=1
        CPU._cycle_count += 1
        CPU._reg_x_history.append(CPU._reg_x)
        if self._cycles_to_complete == 0: # Perform op
            if self._cmd.code == CMD_ADDX.code:
                CPU._reg_x += self._parameter
        print (f"{CPU._cycle_count}: cycles_to_complete:{self._cycles_to_complete} param:{CPU._reg_x} len:{len(CPU._reg_x_history)}")    

    def is_complete(self):
        return self._cycles_to_complete == 0

    def code(self)->str:
        return self._cmd.code

    def parameter(self)->int:
        return self._parameter


class CPU():

    _reg_x_history:list[int] = []
    _reg_x: int = 1
    _cycle_count: int = 0 

    def __init__(self,init_reg_x_value:int):
        self._current_op : Operation  = CMD_BOOTUP
        CPU._reg_x = init_reg_x_value
        CPU._reg_x_history.append(CPU._reg_x)
 
    def parse(self, cmd_code) -> Command:
        if cmd_code == CMD_ADDX.code:
            return CMD_ADDX
        if cmd_code == CMD_NO_OPERATION.code:
            return CMD_NO_OPERATION

    def execute_command(self, cmd: Command, parameter:int = None) :
        self._current_op = Operation(cmd,parameter)
        while not self._current_op.is_complete():
            self._current_op.execute_cycle()

    def get_reg_x_value(self,cycle:int)->int:
        return self._reg_x_history[cycle]
        
