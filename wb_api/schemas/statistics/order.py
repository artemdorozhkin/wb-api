from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Order(BaseModel):
    """
    Модель для представления информации о заказе.

    Attributes:
        date (datetime): Дата и время заказа. Это поле соответствует параметру dateFrom в запросе, если параметр flag=1.
                         Если часовой пояс не указан, то берется Московское время (UTC+3).
        last_change_date (datetime): Дата и время обновления информации в сервисе.
                                     Это поле соответствует параметру dateFrom в запросе, если параметр flag=0 или не указан.
                                     Если часовой пояс не указан, то берется Московское время (UTC+3).
        warehouse_name (str): Склад отгрузки. Максимальная длина - 50 символов.
        country_name (str): Страна. Максимальная длина - 200 символов.
        oblast_okrug_name (str): Округ. Максимальная длина - 200 символов.
        region_name (str): Регион. Максимальная длина - 200 символов.
        supplier_article (str): Артикул продавца. Максимальная длина - 75 символов.
        nm_id (int): Артикул WB.
        barcode (str): Баркод. Максимальная длина - 30 символов.
        category (str): Категория. Максимальная длина - 50 символов.
        subject (str): Предмет. Максимальная длина - 50 символов.
        brand (str): Бренд. Максимальная длина - 50 символов.
        tech_size (str): Размер товара. Максимальная длина - 30 символов.
        income_id (int): Номер поставки.
        is_supply (bool): Договор поставки.
        is_realization (bool): Договор реализации.
        total_price (float): Цена без скидок.
        discount_percent (int): Скидка продавца.
        spp (float): Скидка WB.
        finished_price (float): Цена с учетом всех скидок, кроме суммы по WB Кошельку.
        price_with_disc (float): Цена со скидкой продавца (= totalPrice * (1 - discountPercent/100)).
        is_cancel (bool): Отмена заказа. true - заказ отменен.
        cancel_date (datetime): Дата и время отмены заказа. Если заказ не был отменен, то "0001-01-01T00:00:00".
                                Если часовой пояс не указан, то берется Московское время UTC+3.
        order_type (str): Тип заказа.
        sticker (str): Идентификатор стикера.
        g_number (str): Номер заказа. Максимальная длина - 50 символов.
        srid (str): Уникальный идентификатор заказа.
    """

    date: datetime = Field(
        ...,
        description="Дата и время заказа. Это поле соответствует параметру dateFrom в запросе, если параметр flag=1. Если часовой пояс не указан, то берется Московское время (UTC+3)",
    )
    last_change_date: datetime = Field(
        ...,
        alias="lastChangeDate",
        description="Дата и время обновления информации в сервисе. Это поле соответствует параметру dateFrom в запросе, если параметр flag=0 или не указан. Если часовой пояс не указан, то берется Московское время (UTC+3)",
    )
    warehouse_name: str = Field(
        ..., alias="warehouseName", max_length=50, description="Склад отгрузки"
    )
    country_name: str = Field(
        ..., alias="countryName", max_length=200, description="Страна"
    )
    oblast_okrug_name: str = Field(
        ..., alias="oblastOkrugName", max_length=200, description="Округ"
    )
    region_name: str = Field(
        ..., alias="regionName", max_length=200, description="Регион"
    )
    supplier_article: str = Field(
        ..., alias="supplierArticle", max_length=75, description="Артикул продавца"
    )
    nm_id: int = Field(..., alias="nmId", description="Артикул WB")
    barcode: str = Field(..., max_length=30, description="Баркод")
    category: str = Field(..., max_length=50, description="Категория")
    subject: str = Field(..., max_length=50, description="Предмет")
    brand: str = Field(..., max_length=50, description="Бренд")
    tech_size: str = Field(
        ..., alias="techSize", max_length=30, description="Размер товара"
    )
    income_id: int = Field(..., alias="incomeID", description="Номер поставки")
    is_supply: bool = Field(..., alias="isSupply", description="Договор поставки")
    is_realization: bool = Field(
        ..., alias="isRealization", description="Договор реализации"
    )
    total_price: float = Field(..., alias="totalPrice", description="Цена без скидок")
    discount_percent: int = Field(
        ..., alias="discountPercent", description="Скидка продавца"
    )
    spp: float = Field(..., description="Скидка WB")
    finished_price: float = Field(
        ...,
        alias="finishedPrice",
        description="Цена с учетом всех скидок, кроме суммы по WB Кошельку",
    )
    price_with_disc: float = Field(
        ...,
        alias="priceWithDisc",
        description="Цена со скидкой продавца (= totalPrice * (1 - discountPercent/100))",
    )
    is_cancel: bool = Field(
        ..., alias="isCancel", description="Отмена заказа. true - заказ отменен"
    )
    cancel_date: datetime = Field(
        ...,
        alias="cancelDate",
        description="Дата и время отмены заказа. Если заказ не был отменен, то '0001-01-01T00:00:00'. Если часовой пояс не указан, то берется Московское время UTC+3",
    )
    order_type: Optional[str] = Field(None, alias="orderType", description="Тип заказа")
    sticker: str = Field(..., description="Идентификатор стикера")
    g_number: str = Field(
        ..., alias="gNumber", max_length=50, description="Номер заказа"
    )
    srid: str = Field(..., description="Уникальный идентификатор заказа")

    class Config:
        populate_by_name = True


class Orders(BaseModel):
    orders: List[Order]
