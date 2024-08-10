from typing import List

from pydantic import BaseModel, Field


class Country(BaseModel):
    """
    Модель для представления характеристики Страна Производства.

    Attributes:
        name (str): Наименование.
        full_name (str): Полное наименование.
    """

    name: str = Field(..., description="Наименование")
    full_name: str = Field(..., alias="fullName", description="Полное наименование")

    class Config:
        populate_by_name = True


class Countries(BaseModel):
    countries: List[Country]
