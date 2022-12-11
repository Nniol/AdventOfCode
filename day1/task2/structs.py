from pydantic.fields import Field
from pydantic.main import BaseModel


class ElfInfo(BaseModel):
    number: int  = Field(...)
    count_food_items: int = Field(...)
    total_caloris: int = Field(...)

