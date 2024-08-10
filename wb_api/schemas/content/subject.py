from typing import List

from pydantic import BaseModel, Field


class Subject(BaseModel):
    """
    Модель для представления родительских категорий товаров.

    Attributes:
        subject_id (int): ID подкатегории.
        parent_id (int): ID категории.
        subject_name (str): Наименование подкатегории.
        parent_name (str): Наименование категории.
    """

    subject_id: int = Field(..., alias="subjectID", description="ID подкатегории")
    parent_id: int = Field(..., alias="parentID", description="ID категории")
    subject_name: str = Field(
        ..., alias="subjectName", description="Наименование подкатегории"
    )
    parent_name: str = Field(
        ..., alias="parentName", description="Наименование категории"
    )

    class Config:
        populate_by_name = True


class Subjects(BaseModel):
    subjects: List[Subject]
