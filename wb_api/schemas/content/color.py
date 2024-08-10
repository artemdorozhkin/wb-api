from typing import List

from pydantic import BaseModel, Field


class Color(BaseModel):
    """
    Модель для представления характеристики цвет.

    Attributes:
        name (str): Название цвета.
        parent_name (str): Наименование категории.
    """

    name: str = Field(..., description="Название цвета")
    parent_name: str = Field(
        ..., alias="parentName", description="Наименование категории"
    )

    class Config:
        populate_by_name = True


class Colors(BaseModel):
    colors: List[Color]
