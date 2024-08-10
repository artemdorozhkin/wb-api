from typing import List

from pydantic import BaseModel, Field


class TNVED(BaseModel):
    """
    Модель для представления характеристики Страна Производства.

    Attributes:
        tnved (str): Код ТНВЭД.
        is_kiz (str): Признак КИЗ.
    """

    tnved: str = Field(..., description="Код ТНВЭД")
    is_kiz: str = Field(..., alias="isKiz", description="Признак КИЗ")

    class Config:
        populate_by_name = True


class TNVEDs(BaseModel):
    tnveds: List[TNVED]
