from typing import List

from pydantic import BaseModel, Field


class WarehousePallet(BaseModel):
    """
    Тарифы для монопаллет по складу.

    Attributes:
        pallet_delivery_expr (str): Коэффициент доставки, %. На него умножается стоимость доставки. Во всех тарифах этот коэффициент уже учтён
        pallet_delivery_value_base (str): Доставка 1 литра, ₽
        pallet_delivery_value_liter (float): Доставка каждого дополнительного литра, ₽
        pallet_storage_expr (str): Коэффициент хранения, %. На него умножается стоимость хранения. Во всех тарифах этот коэффициент уже учтён
        pallet_storage_value_expr (str): Хранение 1 монопаллеты, ₽
        warehouse_name (str): Название склада
    """

    pallet_delivery_expr: str = Field(
        ...,
        alias="palletDeliveryExpr",
        description="Коэффициент доставки, %. На него умножается стоимость доставки. Во всех тарифах этот коэффициент уже учтён",
    )
    pallet_delivery_value_base: str = Field(
        ...,
        alias="palletDeliveryValueBase",
        description="Доставка 1 литра, ₽",
    )
    pallet_delivery_value_liter: str = Field(
        ...,
        alias="palletDeliveryValueLiter",
        description="Доставка каждого дополнительного литра, ₽",
    )
    pallet_storage_expr: str = Field(
        ...,
        alias="palletStorageExpr",
        description="Коэффициент хранения, %. На него умножается стоимость хранения. Во всех тарифах этот коэффициент уже учтён",
    )
    pallet_storage_value_expr: str = Field(
        ...,
        alias="palletStorageValueExpr",
        description="Хранение 1 монопаллеты, ₽",
    )
    warehouse_name: str = Field(
        ...,
        alias="warehouseName",
        description="Название склада",
    )


class Pallet(BaseModel):
    """
    Модель тарифов для монопаллет.

    Attributes:
        dt_next_pallet (str): Дата начала следующего тарифа
        dt_till_max (str): Дата окончания последнего установленного тарифа
        warehouse_list (List[WarehousePallet]): Тарифы для монопаллет, сгруппированные по складам
    """

    dt_next_pallet: str = Field(
        ...,
        alias="dtNextPallet",
        description="Дата начала следующего тарифа",
    )
    dt_till_max: str = Field(
        ...,
        alias="dtTillMax",
        description="Дата окончания последнего установленного тарифа",
    )
    warehouse_list: List[WarehousePallet] = Field(
        ...,
        alias="warehouseList",
        description="Тарифы для монопаллет, сгруппированные по складам",
    )

    class Config:
        populate_by_name = True
