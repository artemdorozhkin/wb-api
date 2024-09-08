from typing import List

from pydantic import BaseModel, Field


class WarehouseReturn(BaseModel):
    """
    Тарифы для коробов по складу.

    - стоимость возврата брака и возврата по инициативе продавца при грузовой доставке.
    - стоимость возврата неопознанного складом товара.
    - стоимость возврата брака, возврата по инициативе продавца и автовозвратов Маркетплейс (в пункт выдачи и обратно).

    Можно получить стоимость возврата в пункт выдачи (ПВЗ) и обратной логистики — если продавец не забрал товары из пункта выдачи за 7 дней.

    Attributes:

        deliveryDumpKgtOfficeBase (str):
            Стоимость возврата при грузовой доставке, доставка на ПВЗ (базовая цена за 1 л), ₽

            Применяется для крупногабаритных товаров, когда:
            - продавец хочет вывезти товары со склада Wildberries;
            - на складе обнаружили бракованные товары;
            - покупатель возвращает товар, но его нельзя вернуть в продажу.

        deliveryDumpKgtOfficeLiter (str):
            Стоимость возврата при грузовой доставке, доставка на ПВЗ (доп. литр), ₽
            Стоимость за каждый дополнительный литр.

        deliveryDumpKgtReturnExpr (str):
            Стоимость возврата при грузовой доставке, обратная логистика невостребованного возврата, ₽
            Грузовая доставка невостребованного возврата обратно на склад Wildberries. За единицу товара.

        deliveryDumpSrgOfficeExpr (str):
            Стоимость возврата неопознанного складом товара за каждую единицу, доставка на ПВЗ, ₽
            Применяется для товаров, которые не смогли принять на складе.

        deliveryDumpSrgReturnExpr (str):
            Стоимость возврата неопознанного складом товара за каждую единицу, обратная логистика невостребованного возврата, ₽
            Доставка невостребованного возврата обратно на склад Wildberries.

        deliveryDumpSupCourierBase (str):
            Стоимость возврата, доставка курьером (базовая цена за 1 л), ₽
            Применяется, когда:
            - продавец хочет вывезти товары со склада Wildberries
            - на складе обнаружили бракованные товары
            - покупатель возвращает товар, но его нельзя вернуть в продажу
            - подключён автовозврат товаров, продаваемых по схеме Маркетплейс

        deliveryDumpSupCourierLiter (str):
            Стоимость возврата, доставка курьером (доп. л), ₽
            Стоимость за каждый дополнительный литр.

        deliveryDumpSupOfficeBase (str):
            Стоимость возврата, доставка на ПВЗ (базовая цена за 1 л), ₽
            Применяется, когда:
            - продавец хочет вывезти товары со склада Wildberries
            - на складе обнаружили бракованные товары
            - покупатель возвращает товар, но его нельзя вернуть в продажу
            - подключён автовозврат товаров, продаваемых по схеме Маркетплейс

        deliveryDumpSupOfficeLiter (str):
            Стоимость возврата, доставка на ПВЗ (доп. литр), ₽
            Стоимость за каждый дополнительный литр

        deliveryDumpSupReturnExpr (str):
            Стоимость возврата, обратная логистика невостребованного возврата, за единицу товара, ₽
            Доставка невостребованного возврата обратно на склад Wildberries.
            Применяется, когда:
            - продавец хочет вывезти товары со склада Wildberries
            - на складе обнаружили бракованные товары
            - покупатель возвращает товар, но его нельзя вернуть в продажу
            - подключён автовозврат товаров, продаваемых по схеме Маркетплейс

        warehouseName (str): Название склада
    """

    delivery_dump_kgt_office_base: str = Field(
        ...,
        alias="deliveryDumpKgtOfficeBase",
    )
    delivery_dump_kgt_office_liter: str = Field(
        ...,
        alias="deliveryDumpKgtOfficeLiter",
    )
    delivery_dump_kgt_return_expr: str = Field(
        ...,
        alias="deliveryDumpKgtReturnExpr",
    )
    delivery_dump_srg_office_expr: str = Field(
        ...,
        alias="deliveryDumpSrgOfficeExpr",
    )
    delivery_dump_srg_return_expr: str = Field(
        ...,
        alias="deliveryDumpSrgReturnExpr",
    )
    delivery_dump_sup_courier_base: str = Field(
        ...,
        alias="deliveryDumpSupCourierBase",
    )
    delivery_dump_sup_courier_liter: str = Field(
        ...,
        alias="deliveryDumpSupCourierLiter",
    )
    delivery_dump_sup_office_base: str = Field(
        ...,
        alias="deliveryDumpSupOfficeBase",
    )
    delivery_dump_sup_office_liter: str = Field(
        ...,
        alias="deliveryDumpSupOfficeLiter",
    )
    delivery_dump_sup_return_expr: str = Field(
        ...,
        alias="deliveryDumpSupReturnExpr",
    )
    warehouse_name: str = Field(
        ...,
        alias="warehouseName",
        description="Название склада",
    )


class Return(BaseModel):
    """
    Модель тарифов на возврат.

    Attributes:
        dt_next_box (str): Дата начала следующего тарифа при грузовой доставке
        dt_next_box (str): Дата начала следующего тарифа для неопознанных товаров
        dt_next_box (str): Дата начала следующего тарифа при обычной доставке
        warehouse_list (List[WarehouseBox]): Тарифы на возврат, сгруппированные по складам
    """

    dt_next_delivery_dump_kgt: str = Field(
        ...,
        alias="dtNextDeliveryDumpKgt",
        description="Дата начала следующего тарифа при грузовой доставке",
    )
    dt_next_delivery_dump_srg: str = Field(
        ...,
        alias="dtNextDeliveryDumpSrg",
        description="Дата начала следующего тарифа для неопознанных товаров",
    )
    dt_next_delivery_dump_sup: str = Field(
        ...,
        alias="dtNextDeliveryDumpSup",
        description="Дата начала следующего тарифа при обычной доставке",
    )
    warehouse_list: List[WarehouseReturn] = Field(
        ...,
        alias="warehouseList",
        description="Тарифы для коробов, сгруппированные по складам",
    )

    class Config:
        populate_by_name = True
