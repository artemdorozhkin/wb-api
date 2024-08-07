from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class Stock(BaseModel):
    """
    Модель для представления информации о складе.

    Attributes:
        last_change_date (datetime): Дата и время обновления информации в сервисе.
                                     Это поле соответствует параметру dateFrom в запросе.
                                     Если часовой пояс не указан, то берется Московское время (UTC+3).
        warehouse_name (str): Название склада. Максимальная длина - 50 символов.
        supplier_article (str): Артикул продавца. Максимальная длина - 75 символов.
        nm_id (int): Артикул WB.
        barcode (str): Баркод. Максимальная длина - 30 символов.
        quantity (int): Количество, доступное для продажи (сколько можно добавить в корзину).
        in_way_to_client (int): В пути к клиенту.
        in_way_from_client (int): В пути от клиента.
        quantity_full (int): Полное (непроданное) количество, которое числится за складом (= quantity + в пути).
        category (str): Категория. Максимальная длина - 50 символов.
        subject (str): Предмет. Максимальная длина - 50 символов.
        brand (str): Бренд. Максимальная длина - 50 символов.
        tech_size (str): Размер. Максимальная длина - 30 символов.
        price (float): Цена.
        discount (float): Скидка.
        is_supply (bool): Договор поставки (внутренние технологические данные).
        is_realization (bool): Договор реализации (внутренние технологические данные).
        sc_code (str): Код контракта (внутренние технологические данные). Максимальная длина - 50 символов.
    """

    last_change_date: datetime = Field(
        ...,
        alias="lastChangeDate",
        description="Дата и время обновления информации в сервисе. Это поле соответствует параметру dateFrom в запросе. Если часовой пояс не указан, то берется Московское время (UTC+3)",
    )
    warehouse_name: str = Field(
        ..., alias="warehouseName", max_length=50, description="Название склада"
    )
    supplier_article: str = Field(
        ..., alias="supplierArticle", max_length=75, description="Артикул продавца"
    )
    nm_id: int = Field(..., alias="nmId", description="Артикул WB")
    barcode: str = Field(..., max_length=30, description="Баркод")
    quantity: int = Field(
        ...,
        description="Количество, доступное для продажи (сколько можно добавить в корзину)",
    )
    in_way_to_client: int = Field(
        ..., alias="inWayToClient", description="В пути к клиенту"
    )
    in_way_from_client: int = Field(
        ..., alias="inWayFromClient", description="В пути от клиента"
    )
    quantity_full: int = Field(
        ...,
        alias="quantityFull",
        description="Полное (непроданное) количество, которое числится за складом (= quantity + в пути)",
    )
    category: str = Field(..., max_length=50, description="Категория")
    subject: str = Field(..., max_length=50, description="Предмет")
    brand: str = Field(..., max_length=50, description="Бренд")
    tech_size: str = Field(..., alias="techSize", max_length=30, description="Размер")
    price: float = Field(..., alias="Price", description="Цена")
    discount: float = Field(..., alias="Discount", description="Скидка")
    is_supply: bool = Field(
        ...,
        alias="isSupply",
        description="Договор поставки (внутренние технологические данные)",
    )
    is_realization: bool = Field(
        ...,
        alias="isRealization",
        description="Договор реализации (внутренние технологические данные)",
    )
    sc_code: str = Field(
        ...,
        alias="SCCode",
        max_length=50,
        description="Код контракта (внутренние технологические данные)",
    )

    class Config:
        populate_by_name = True


class Stocks(BaseModel):
    stocks: List[Stock]
