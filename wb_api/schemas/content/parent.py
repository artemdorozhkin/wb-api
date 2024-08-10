from typing import List

from pydantic import BaseModel, Field


class Parent(BaseModel):
    """
    Модель для представления родительских категорий товаров.

    Attributes:
        id (int): ID категории.
        name (str): Наименование категории.
        is_visible (bool): Видимость.
    """

    id: int = Field(..., description="Номер поставки")
    name: str = Field(..., description="Номер УПД")
    is_visible: bool = Field(
        ...,
        alias="isVisible",
        description="Дата поступления. Если часовой пояс не указан, то берется Московское время UTC+3",
    )

    class Config:
        populate_by_name = True


class Parents(BaseModel):
    parents: List[Parent]
