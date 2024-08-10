{"subjectID": 105, "parentID": 2, "subjectName": "Кроссовки", "parentName": "Обувь"},

from typing import List

from pydantic import BaseModel, Field


class Charc(BaseModel):
    """
    Модель для представления характеристик предмета.

    Attributes:
        charc_id (int): ID характеристики
        subject_name (str): Наименование подкатегории
        subject_id (int): ID подкатегории
        name (str): Наименование характеристики
        required (bool): -
        unit_name (str): -
        max_count (int): -
        popular (bool): -
        charc_type (int): -
    """

    charc_id: int = Field(..., alias="charcID", description="ID характеристики")
    subject_name: str = Field(
        ..., alias="subjectName", description="Наименование подкатегории"
    )
    subject_id: int = Field(..., alias="subjectID", description="ID подкатегории")
    name: str = Field(..., description="Наименование характеристики")
    required: bool = Field(..., description="Обязательно")
    unit_name: str = Field(..., alias="unitName")
    max_count: int = Field(..., alias="maxCount")
    popular: bool = Field(...)
    charc_type: int = Field(..., alias="charcType")

    class Config:
        populate_by_name = True


class Charcs(BaseModel):
    charcs: List[Charc]
