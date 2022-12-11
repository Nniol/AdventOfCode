from pydantic.fields import Field
from pydantic.main import BaseModel
from typing import Literal

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

LOSE ='Lose'
DRAW = 'Daw'
WIN ='Win'

opp_shape_code_list = Literal['A','B','C']
my_shape_code_list=desired_result_list = Literal['X','Y','Z']

opp_shape_dict = {
    'A':ROCK,
    'B':PAPER,
    'C':SCISSORS,
}

my_shape_dict = {
    'X':ROCK,
    'Y':PAPER,
    'Z':SCISSORS,
}

my_desired_result_dict = {
    'X':LOSE,
    'Y':DRAW,
    'Z':WIN,
}


shape_points={
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

shapes_for_result = {
    ROCK: {
        WIN: PAPER,
        LOSE: SCISSORS,
        DRAW: ROCK
    },
    PAPER: {
        WIN: SCISSORS,
        LOSE: ROCK,
        DRAW: PAPER
    },
    SCISSORS: {
        WIN: ROCK,
        LOSE: PAPER,
        DRAW: SCISSORS
    }
}

class rps_round(BaseModel):
    opp_shape_code:opp_shape_code_list = Field(...)
    my_code:my_shape_code_list = Field(...)
    points:int = Field(0)


    def play(self)->int:
        opp_shape = opp_shape_dict[self.opp_shape_code]
        my_shape = my_shape_dict[self.my_code]

        self.points = shape_points[my_shape]
        result_points = self.get_round_points(opp_shape=opp_shape, my_shape=my_shape)
        print (f"PLAY: Opp Shape[{opp_shape}]; My Shape[{my_shape}]; Shape Points[{shape_points[my_shape]}]; Result Points[{result_points}]")

        self.points += result_points


        return self.points

    def play_to_result(self)->int:
        opp_shape = opp_shape_dict[self.opp_shape_code]
        desired_result = my_desired_result_dict[self.my_code]
        my_shape = shapes_for_result[opp_shape][desired_result]

        self.points = shape_points[my_shape]
        result_points = self.get_round_points(opp_shape=opp_shape, my_shape=my_shape)
        print (f"PTR: Opp Shape[{opp_shape}]; My Shape[{my_shape}]; Shape Points[{shape_points[my_shape]}]; Result Points[{result_points}]")

        self.points += result_points
        return self.points


    def get_round_points(self,opp_shape:str,my_shape:str) -> int:
        if opp_shape == my_shape:
            return 3
        if my_shape == ROCK and opp_shape == SCISSORS:
            return 6
        if my_shape == PAPER and opp_shape == ROCK:
            return 6
        if my_shape == SCISSORS and opp_shape == PAPER:
            return 6

        return 0