from typing import List

from pydantic import BaseModel, Field


class WarehouseBox(BaseModel):
    """
    Тарифы для коробов по складу.

    Attributes:
        boxDeliveryAndStorageExpr (str): Коэффициент, %. На него умножается стоимость доставки и хранения. Во всех тарифах этот коэффициент уже учтён
        boxDeliveryBase (str): Доставка 1 литра, ₽
        boxDeliveryLiter (float): Доставка каждого дополнительного литра, ₽
        boxStorageBase (str): Хранение 1 литра, ₽
        boxStorageLiter (str): Хранение каждого дополнительного литра, ₽
        warehouseName (str): Название склада
    """

    box_delivery_and_storage_expr: str = Field(
        ...,
        alias="boxDeliveryAndStorageExpr",
        description="Коэффициент, %. На него умножается стоимость доставки и хранения. Во всех тарифах этот коэффициент уже учтён",
    )
    box_delivery_base: str = Field(
        ...,
        alias="boxDeliveryBase",
        description="Доставка 1 литра, ₽",
    )
    box_delivery_liter: str = Field(
        ...,
        alias="boxDeliveryLiter",
        description="Доставка каждого дополнительного литра, ₽",
    )
    box_storage_base: str = Field(
        ...,
        alias="boxStorageBase",
        description="Хранение 1 литра, ₽",
    )
    box_storage_liter: str = Field(
        ...,
        alias="boxStorageLiter",
        description="Хранение каждого дополнительного литра, ₽",
    )
    warehouse_name: str = Field(
        ...,
        alias="warehouseName",
        description="Название склада",
    )


class Box(BaseModel):
    """
    Модель комиссии по категориям товаров.

    Attributes:
        dt_next_box (str): Дата начала следующего тарифа
        dt_till_max (str): Дата окончания последнего установленного тарифа
        warehouse_list (float): Тарифы для коробов, сгруппированные по складам
    """

    dt_next_box: str = Field(
        ...,
        alias="dtNextBox",
        description="Дата начала следующего тарифа",
    )
    dt_till_max: str = Field(
        ...,
        alias="dtTillMax",
        description="Дата окончания последнего установленного тарифа",
    )
    warehouse_list: List[WarehouseBox] = Field(
        ...,
        alias="warehouseList",
        description="Тарифы для коробов, сгруппированные по складам",
    )

    class Config:
        populate_by_name = True
